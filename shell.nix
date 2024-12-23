{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
	packages = [ 
		pkgs.python312
		pkgs.python312Packages.scrapy
		pkgs.python312Packages.colorlog
		pkgs.python312Packages.python-dotenv
	];

	shellHook = ''
		echo "ISTransfere shell initialized"
	'';
}
