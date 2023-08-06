{
  description = "Singer io SDK with strict types";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    nix_filter.url = "github:numtide/nix-filter";
    purity.url = "gitlab:dmurciaatfluid/purity?ref=v1.31.0";
    purity.inputs.nixpkgs.follows = "nixpkgs";
    purity.inputs.nix_filter.follows = "nix_filter";
  };
  outputs = {
    self,
    nixpkgs,
    nix_filter,
    purity,
  }: let
    system = "x86_64-linux";
    metadata = (builtins.fromTOML (builtins.readFile ./pyproject.toml)).project;
    path_filter = nix_filter.outputs.lib;
    src = path_filter {
      root = self;
      include = [
        "arch.cfg"
        "arch_test.cfg"
        "pyproject.toml"
        (path_filter.inDirectory metadata.name)
        (path_filter.inDirectory "tests")
      ];
    };
    out = import ./build {
      inherit src;
      nixpkgs =
        nixpkgs.legacyPackages."${system}"
        // {
          purity = purity.packages."${system}";
        };
    };
  in {
    packages."${system}" = out;
    defaultPackage."${system}" = self.packages."${system}".python39.pkg;
  };
}
