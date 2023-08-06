{
  lib,
  python_pkgs,
}: let
  utils = import ./override_utils.nix;
  pkgs_overrides = override: python_pkgs: builtins.mapAttrs (_: override python_pkgs) python_pkgs;

  layer_1 = python_pkgs:
    python_pkgs
    // {
      import-linter = import ./import-linter {
        inherit lib;
        click = python_pkgs.click;
        networkx = python_pkgs.networkx;
      };
      jsonschema = python_pkgs.jsonschema.overridePythonAttrs (
        old: rec {
          version = "3.2.0";
          SETUPTOOLS_SCM_PRETEND_VERSION = version;
          src = lib.fetchPypi {
            inherit version;
            pname = old.pname;
            sha256 = "yKhbKNN3zHc35G4tnytPRO48Dh3qxr9G3e/HGH0weXo=";
          };
          doCheck = false;
        }
      );
      pyrsistent = python_pkgs.pyrsistent.overridePythonAttrs (
        _: {doCheck = false;}
      );
      types-jsonschema = import ./jsonschema/stubs.nix lib;
      types-pyRFC3339 = import ./pyRFC3339/stubs.nix lib;
    };

  pyrsistent_override = python_pkgs: utils.replace_pkg ["pyrsistent"] python_pkgs.pyrsistent;
  networkx_override = python_pkgs: utils.replace_pkg ["networkx"] (import ./networkx.nix lib python_pkgs);
  overrides = map pkgs_overrides [
    pyrsistent_override
    networkx_override
  ];

  final_pkgs = utils.compose ([layer_1] ++ overrides) python_pkgs;
in {
  python_pkgs = final_pkgs;
}
