/*
 Originally taken from JSManage
*/

// requirements
var fs = require('fs');
import System.IO;
import System;

var logFilePath = "../modules/browser_info.json"

/*
 Function purpose: Get navigator information to determine necessary needs
 Inputs: None
 Outputs:
 	isp() => the web browsers vendor
 	userAgent() => the web browsers user agent
 	platform() => the web browsers platform / OS
 	userLanguage() => the web browsers language, typically preferred user language
*/
class get_navigator_information {
	get_isp() {
		return navigator.vendor
	}

	userAgent() {
		return navigator.userAgent
	}

	platform() {
		return navigator.platform
	}

	userLanguage() {
		return navigator.languages
	}
}

let gni = new get_navigator_information();

function writeToFile(logFilePath : String) {
    var sw = new StreamWriter(logFilePath);
    sw.WriteLine(get_navigator_information.get_isp());
    sw.WriteLine(get_navigator_information.userAgent());
    sw.WriteLine(get_navigator_information.platform());
    sw.WriteLine(get_navigator_information.userLanguage());
  }
}
