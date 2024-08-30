{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    venv = {
      enable = true;
      requirements = (builtins.readFile ./requirements.txt);
    };
  };
}
