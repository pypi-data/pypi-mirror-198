{
  src,
  nixpkgs,
}: let
  supported = ["python38" "python39" "python310" "python311"];
  metadata = let
    _metadata = (builtins.fromTOML (builtins.readFile "${src}/pyproject.toml")).project;
    file_str = builtins.readFile "${src}/${_metadata.name}/__init__.py";
    match = builtins.match ".*__version__ *= *\"(.+?)\"\n.*" file_str;
    version = builtins.elemAt match 0;
  in
    _metadata // {inherit version;};
  publish = import ./publish {
    inherit nixpkgs;
  };
  build_pkg = {
    lib,
    python_pkgs,
  }:
    import ./pkg {
      inherit lib metadata python_pkgs src;
    };
  build_for = python_version: let
    lib = {
      buildEnv = nixpkgs."${python_version}".buildEnv.override;
      buildPythonPackage = nixpkgs."${python_version}".pkgs.buildPythonPackage;
      fetchPypi = nixpkgs.python3Packages.fetchPypi;
    };
    python_pkgs =
      nixpkgs."${python_version}Packages"
      // {
        fa-purity = nixpkgs.purity."${python_version}".pkg;
      };
    deps = import ./deps {inherit lib python_pkgs;};
    self_pkgs = build_pkg {
      inherit lib;
      python_pkgs = deps.python_pkgs;
    };
    checks = import ./ci/check.nix {self_pkg = self_pkgs.pkg;};
  in {
    check = checks;
    env = self_pkgs.env;
    pkg = self_pkgs.pkg;
  };

  pkgs = builtins.listToAttrs (map
    (name: {
      inherit name;
      value = build_for name;
    })
    supported);
in
  pkgs
  // {
    inherit build_pkg publish;
  }
