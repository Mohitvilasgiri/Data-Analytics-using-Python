<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>C:\Users\MOHIT VILAS GIRI\Desktop\Internship 2020</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Analysis-of-Meteorological-Data">Analysis of Meteorological Data<a class="anchor-link" href="#Analysis-of-Meteorological-Data">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[173]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[174]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span> <span class="o">=</span><span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;C:/Users/MOHIT VILAS GIRI/Desktop/Internship 2020/weatherHistory.csv&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[175]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[175]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-04-01 00:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.472222</td>
      <td>7.388889</td>
      <td>0.89</td>
      <td>14.1197</td>
      <td>251.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.13</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-04-01 01:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>7.227778</td>
      <td>0.86</td>
      <td>14.2646</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.63</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2006-04-01 02:00:00.000 +0200</td>
      <td>Mostly Cloudy</td>
      <td>rain</td>
      <td>9.377778</td>
      <td>9.377778</td>
      <td>0.89</td>
      <td>3.9284</td>
      <td>204.0</td>
      <td>14.9569</td>
      <td>0.0</td>
      <td>1015.94</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2006-04-01 03:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>8.288889</td>
      <td>5.944444</td>
      <td>0.83</td>
      <td>14.1036</td>
      <td>269.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1016.41</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006-04-01 04:00:00.000 +0200</td>
      <td>Mostly Cloudy</td>
      <td>rain</td>
      <td>8.755556</td>
      <td>6.977778</td>
      <td>0.83</td>
      <td>11.0446</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1016.51</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006-04-01 05:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.222222</td>
      <td>7.111111</td>
      <td>0.85</td>
      <td>13.9587</td>
      <td>258.0</td>
      <td>14.9569</td>
      <td>0.0</td>
      <td>1016.66</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2006-04-01 06:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>7.733333</td>
      <td>5.522222</td>
      <td>0.95</td>
      <td>12.3648</td>
      <td>259.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1016.72</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2006-04-01 07:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>8.772222</td>
      <td>6.527778</td>
      <td>0.89</td>
      <td>14.1519</td>
      <td>260.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1016.84</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2006-04-01 08:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>10.822222</td>
      <td>10.822222</td>
      <td>0.82</td>
      <td>11.3183</td>
      <td>259.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1017.37</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2006-04-01 09:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>13.772222</td>
      <td>13.772222</td>
      <td>0.72</td>
      <td>12.5258</td>
      <td>279.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1017.22</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[176]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[176]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(96453, 12)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[177]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[177]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>96453.000000</td>
      <td>96453.000000</td>
      <td>96453.000000</td>
      <td>96453.000000</td>
      <td>96453.000000</td>
      <td>96453.000000</td>
      <td>96453.0</td>
      <td>96453.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>11.932678</td>
      <td>10.855029</td>
      <td>0.734899</td>
      <td>10.810640</td>
      <td>187.509232</td>
      <td>10.347325</td>
      <td>0.0</td>
      <td>1003.235956</td>
    </tr>
    <tr>
      <th>std</th>
      <td>9.551546</td>
      <td>10.696847</td>
      <td>0.195473</td>
      <td>6.913571</td>
      <td>107.383428</td>
      <td>4.192123</td>
      <td>0.0</td>
      <td>116.969906</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-21.822222</td>
      <td>-27.716667</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.688889</td>
      <td>2.311111</td>
      <td>0.600000</td>
      <td>5.828200</td>
      <td>116.000000</td>
      <td>8.339800</td>
      <td>0.0</td>
      <td>1011.900000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>12.000000</td>
      <td>12.000000</td>
      <td>0.780000</td>
      <td>9.965900</td>
      <td>180.000000</td>
      <td>10.046400</td>
      <td>0.0</td>
      <td>1016.450000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>18.838889</td>
      <td>18.838889</td>
      <td>0.890000</td>
      <td>14.135800</td>
      <td>290.000000</td>
      <td>14.812000</td>
      <td>0.0</td>
      <td>1021.090000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>39.905556</td>
      <td>39.344444</td>
      <td>1.000000</td>
      <td>63.852600</td>
      <td>359.000000</td>
      <td>16.100000</td>
      <td>0.0</td>
      <td>1046.380000</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[178]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">columns</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[178]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Index([&#39;Formatted Date&#39;, &#39;Summary&#39;, &#39;Precip Type&#39;, &#39;Temperature (C)&#39;,
       &#39;Apparent Temperature (C)&#39;, &#39;Humidity&#39;, &#39;Wind Speed (km/h)&#39;,
       &#39;Wind Bearing (degrees)&#39;, &#39;Visibility (km)&#39;, &#39;Loud Cover&#39;,
       &#39;Pressure (millibars)&#39;, &#39;Daily Summary&#39;],
      dtype=&#39;object&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[179]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">dtypes</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[179]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Formatted Date               object
Summary                      object
Precip Type                  object
Temperature (C)             float64
Apparent Temperature (C)    float64
Humidity                    float64
Wind Speed (km/h)           float64
Wind Bearing (degrees)      float64
Visibility (km)             float64
Loud Cover                  float64
Pressure (millibars)        float64
Daily Summary                object
dtype: object</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[180]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Summary&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[180]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([&#39;Partly Cloudy&#39;, &#39;Mostly Cloudy&#39;, &#39;Overcast&#39;, &#39;Foggy&#39;,
       &#39;Breezy and Mostly Cloudy&#39;, &#39;Clear&#39;, &#39;Breezy and Partly Cloudy&#39;,
       &#39;Breezy and Overcast&#39;, &#39;Humid and Mostly Cloudy&#39;,
       &#39;Humid and Partly Cloudy&#39;, &#39;Windy and Foggy&#39;, &#39;Windy and Overcast&#39;,
       &#39;Breezy and Foggy&#39;, &#39;Windy and Partly Cloudy&#39;, &#39;Breezy&#39;,
       &#39;Dry and Partly Cloudy&#39;, &#39;Windy and Mostly Cloudy&#39;,
       &#39;Dangerously Windy and Partly Cloudy&#39;, &#39;Dry&#39;, &#39;Windy&#39;,
       &#39;Humid and Overcast&#39;, &#39;Light Rain&#39;, &#39;Drizzle&#39;, &#39;Windy and Dry&#39;,
       &#39;Dry and Mostly Cloudy&#39;, &#39;Breezy and Dry&#39;, &#39;Rain&#39;], dtype=object)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[181]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">nunique</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[181]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;bound method DataFrame.nunique of                       Formatted Date        Summary Precip Type  \
0      2006-04-01 00:00:00.000 +0200  Partly Cloudy        rain   
1      2006-04-01 01:00:00.000 +0200  Partly Cloudy        rain   
2      2006-04-01 02:00:00.000 +0200  Mostly Cloudy        rain   
3      2006-04-01 03:00:00.000 +0200  Partly Cloudy        rain   
4      2006-04-01 04:00:00.000 +0200  Mostly Cloudy        rain   
...                              ...            ...         ...   
96448  2016-09-09 19:00:00.000 +0200  Partly Cloudy        rain   
96449  2016-09-09 20:00:00.000 +0200  Partly Cloudy        rain   
96450  2016-09-09 21:00:00.000 +0200  Partly Cloudy        rain   
96451  2016-09-09 22:00:00.000 +0200  Partly Cloudy        rain   
96452  2016-09-09 23:00:00.000 +0200  Partly Cloudy        rain   

       Temperature (C)  Apparent Temperature (C)  Humidity  Wind Speed (km/h)  \
0             9.472222                  7.388889      0.89            14.1197   
1             9.355556                  7.227778      0.86            14.2646   
2             9.377778                  9.377778      0.89             3.9284   
3             8.288889                  5.944444      0.83            14.1036   
4             8.755556                  6.977778      0.83            11.0446   
...                ...                       ...       ...                ...   
96448        26.016667                 26.016667      0.43            10.9963   
96449        24.583333                 24.583333      0.48            10.0947   
96450        22.038889                 22.038889      0.56             8.9838   
96451        21.522222                 21.522222      0.60            10.5294   
96452        20.438889                 20.438889      0.61             5.8765   

       Wind Bearing (degrees)  Visibility (km)  Loud Cover  \
0                       251.0          15.8263         0.0   
1                       259.0          15.8263         0.0   
2                       204.0          14.9569         0.0   
3                       269.0          15.8263         0.0   
4                       259.0          15.8263         0.0   
...                       ...              ...         ...   
96448                    31.0          16.1000         0.0   
96449                    20.0          15.5526         0.0   
96450                    30.0          16.1000         0.0   
96451                    20.0          16.1000         0.0   
96452                    39.0          15.5204         0.0   

       Pressure (millibars)                           Daily Summary  
0                   1015.13       Partly cloudy throughout the day.  
1                   1015.63       Partly cloudy throughout the day.  
2                   1015.94       Partly cloudy throughout the day.  
3                   1016.41       Partly cloudy throughout the day.  
4                   1016.51       Partly cloudy throughout the day.  
...                     ...                                     ...  
96448               1014.36  Partly cloudy starting in the morning.  
96449               1015.16  Partly cloudy starting in the morning.  
96450               1015.66  Partly cloudy starting in the morning.  
96451               1015.95  Partly cloudy starting in the morning.  
96452               1016.16  Partly cloudy starting in the morning.  

[96453 rows x 12 columns]&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[182]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">count</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[182]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;bound method DataFrame.count of                       Formatted Date        Summary Precip Type  \
0      2006-04-01 00:00:00.000 +0200  Partly Cloudy        rain   
1      2006-04-01 01:00:00.000 +0200  Partly Cloudy        rain   
2      2006-04-01 02:00:00.000 +0200  Mostly Cloudy        rain   
3      2006-04-01 03:00:00.000 +0200  Partly Cloudy        rain   
4      2006-04-01 04:00:00.000 +0200  Mostly Cloudy        rain   
...                              ...            ...         ...   
96448  2016-09-09 19:00:00.000 +0200  Partly Cloudy        rain   
96449  2016-09-09 20:00:00.000 +0200  Partly Cloudy        rain   
96450  2016-09-09 21:00:00.000 +0200  Partly Cloudy        rain   
96451  2016-09-09 22:00:00.000 +0200  Partly Cloudy        rain   
96452  2016-09-09 23:00:00.000 +0200  Partly Cloudy        rain   

       Temperature (C)  Apparent Temperature (C)  Humidity  Wind Speed (km/h)  \
0             9.472222                  7.388889      0.89            14.1197   
1             9.355556                  7.227778      0.86            14.2646   
2             9.377778                  9.377778      0.89             3.9284   
3             8.288889                  5.944444      0.83            14.1036   
4             8.755556                  6.977778      0.83            11.0446   
...                ...                       ...       ...                ...   
96448        26.016667                 26.016667      0.43            10.9963   
96449        24.583333                 24.583333      0.48            10.0947   
96450        22.038889                 22.038889      0.56             8.9838   
96451        21.522222                 21.522222      0.60            10.5294   
96452        20.438889                 20.438889      0.61             5.8765   

       Wind Bearing (degrees)  Visibility (km)  Loud Cover  \
0                       251.0          15.8263         0.0   
1                       259.0          15.8263         0.0   
2                       204.0          14.9569         0.0   
3                       269.0          15.8263         0.0   
4                       259.0          15.8263         0.0   
...                       ...              ...         ...   
96448                    31.0          16.1000         0.0   
96449                    20.0          15.5526         0.0   
96450                    30.0          16.1000         0.0   
96451                    20.0          16.1000         0.0   
96452                    39.0          15.5204         0.0   

       Pressure (millibars)                           Daily Summary  
0                   1015.13       Partly cloudy throughout the day.  
1                   1015.63       Partly cloudy throughout the day.  
2                   1015.94       Partly cloudy throughout the day.  
3                   1016.41       Partly cloudy throughout the day.  
4                   1016.51       Partly cloudy throughout the day.  
...                     ...                                     ...  
96448               1014.36  Partly cloudy starting in the morning.  
96449               1015.16  Partly cloudy starting in the morning.  
96450               1015.66  Partly cloudy starting in the morning.  
96451               1015.95  Partly cloudy starting in the morning.  
96452               1016.16  Partly cloudy starting in the morning.  

[96453 rows x 12 columns]&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[183]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Summary&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[183]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;bound method IndexOpsMixin.value_counts of 0        Partly Cloudy
1        Partly Cloudy
2        Mostly Cloudy
3        Partly Cloudy
4        Mostly Cloudy
             ...      
96448    Partly Cloudy
96449    Partly Cloudy
96450    Partly Cloudy
96451    Partly Cloudy
96452    Partly Cloudy
Name: Summary, Length: 96453, dtype: object&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[184]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 96453 entries, 0 to 96452
Data columns (total 12 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Formatted Date            96453 non-null  object 
 1   Summary                   96453 non-null  object 
 2   Precip Type               95936 non-null  object 
 3   Temperature (C)           96453 non-null  float64
 4   Apparent Temperature (C)  96453 non-null  float64
 5   Humidity                  96453 non-null  float64
 6   Wind Speed (km/h)         96453 non-null  float64
 7   Wind Bearing (degrees)    96453 non-null  float64
 8   Visibility (km)           96453 non-null  float64
 9   Loud Cover                96453 non-null  float64
 10  Pressure (millibars)      96453 non-null  float64
 11  Daily Summary             96453 non-null  object 
dtypes: float64(8), object(4)
memory usage: 8.8+ MB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[185]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[185]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-04-01 00:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.472222</td>
      <td>7.388889</td>
      <td>0.89</td>
      <td>14.1197</td>
      <td>251.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.13</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-04-01 01:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>7.227778</td>
      <td>0.86</td>
      <td>14.2646</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.63</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2006-04-01 02:00:00.000 +0200</td>
      <td>Mostly Cloudy</td>
      <td>rain</td>
      <td>9.377778</td>
      <td>9.377778</td>
      <td>0.89</td>
      <td>3.9284</td>
      <td>204.0</td>
      <td>14.9569</td>
      <td>0.0</td>
      <td>1015.94</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2006-04-01 03:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>8.288889</td>
      <td>5.944444</td>
      <td>0.83</td>
      <td>14.1036</td>
      <td>269.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1016.41</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006-04-01 04:00:00.000 +0200</td>
      <td>Mostly Cloudy</td>
      <td>rain</td>
      <td>8.755556</td>
      <td>6.977778</td>
      <td>0.83</td>
      <td>11.0446</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1016.51</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006-04-01 05:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.222222</td>
      <td>7.111111</td>
      <td>0.85</td>
      <td>13.9587</td>
      <td>258.0</td>
      <td>14.9569</td>
      <td>0.0</td>
      <td>1016.66</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2006-04-01 06:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>7.733333</td>
      <td>5.522222</td>
      <td>0.95</td>
      <td>12.3648</td>
      <td>259.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1016.72</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2006-04-01 07:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>8.772222</td>
      <td>6.527778</td>
      <td>0.89</td>
      <td>14.1519</td>
      <td>260.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1016.84</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2006-04-01 08:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>10.822222</td>
      <td>10.822222</td>
      <td>0.82</td>
      <td>11.3183</td>
      <td>259.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1017.37</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2006-04-01 09:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>13.772222</td>
      <td>13.772222</td>
      <td>0.72</td>
      <td>12.5258</td>
      <td>279.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1017.22</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[186]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[186]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Formatted Date              96429
Summary                        27
Precip Type                     2
Temperature (C)              7574
Apparent Temperature (C)     8984
Humidity                       90
Wind Speed (km/h)            2484
Wind Bearing (degrees)        360
Visibility (km)               949
Loud Cover                      1
Pressure (millibars)         4979
Daily Summary                 214
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[187]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Wind Speed (km/h)&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[187]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>2484</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[188]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Wind Speed (km/h)&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[188]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([14.1197, 14.2646,  3.9284, ..., 37.0622, 35.5971, 30.751 ])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Number-of-time-when-the-Weather-mostly-clear">Number of time when the Weather mostly clear<a class="anchor-link" href="#Number-of-time-when-the-Weather-mostly-clear">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[189]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[189]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-04-01 00:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.472222</td>
      <td>7.388889</td>
      <td>0.89</td>
      <td>14.1197</td>
      <td>251.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.13</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-04-01 01:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>7.227778</td>
      <td>0.86</td>
      <td>14.2646</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.63</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[190]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">Summary</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[190]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Partly Cloudy                          31733
Mostly Cloudy                          28094
Overcast                               16597
Clear                                  10890
Foggy                                   7148
Breezy and Overcast                      528
Breezy and Mostly Cloudy                 516
Breezy and Partly Cloudy                 386
Dry and Partly Cloudy                     86
Windy and Partly Cloudy                   67
Light Rain                                63
Breezy                                    54
Windy and Overcast                        45
Humid and Mostly Cloudy                   40
Drizzle                                   39
Windy and Mostly Cloudy                   35
Breezy and Foggy                          35
Dry                                       34
Humid and Partly Cloudy                   17
Dry and Mostly Cloudy                     14
Rain                                      10
Windy                                      8
Humid and Overcast                         7
Windy and Foggy                            4
Breezy and Dry                             1
Windy and Dry                              1
Dangerously Windy and Partly Cloudy        1
Name: Summary, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[191]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="n">dataset</span><span class="o">.</span><span class="n">Summary</span><span class="o">==</span> <span class="s1">&#39;Clear&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[191]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>223</th>
      <td>2006-04-18 07:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>8.688889</td>
      <td>8.688889</td>
      <td>0.93</td>
      <td>1.4329</td>
      <td>290.0</td>
      <td>5.8443</td>
      <td>0.0</td>
      <td>1012.96</td>
      <td>Partly cloudy until night.</td>
    </tr>
    <tr>
      <th>309</th>
      <td>2006-04-20 21:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>12.266667</td>
      <td>12.266667</td>
      <td>0.99</td>
      <td>8.0500</td>
      <td>320.0</td>
      <td>6.1985</td>
      <td>0.0</td>
      <td>1015.76</td>
      <td>Foggy starting overnight continuing until morn...</td>
    </tr>
    <tr>
      <th>337</th>
      <td>2006-04-22 01:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>8.633333</td>
      <td>0.96</td>
      <td>6.4239</td>
      <td>321.0</td>
      <td>3.3649</td>
      <td>0.0</td>
      <td>1017.56</td>
      <td>Foggy starting overnight continuing until morn...</td>
    </tr>
    <tr>
      <th>338</th>
      <td>2006-04-22 02:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>9.861111</td>
      <td>9.861111</td>
      <td>0.96</td>
      <td>3.2361</td>
      <td>319.0</td>
      <td>4.4597</td>
      <td>0.0</td>
      <td>1016.16</td>
      <td>Foggy starting overnight continuing until morn...</td>
    </tr>
    <tr>
      <th>357</th>
      <td>2006-04-22 21:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>12.494444</td>
      <td>12.494444</td>
      <td>0.91</td>
      <td>3.9445</td>
      <td>197.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1015.51</td>
      <td>Foggy starting overnight continuing until morn...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>96432</th>
      <td>2016-09-09 03:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>15.594444</td>
      <td>15.594444</td>
      <td>0.87</td>
      <td>3.2844</td>
      <td>41.0</td>
      <td>15.4399</td>
      <td>0.0</td>
      <td>1014.52</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
    <tr>
      <th>96433</th>
      <td>2016-09-09 04:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>15.011111</td>
      <td>15.011111</td>
      <td>0.93</td>
      <td>3.2039</td>
      <td>341.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1014.37</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
    <tr>
      <th>96434</th>
      <td>2016-09-09 05:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>15.016667</td>
      <td>15.016667</td>
      <td>0.90</td>
      <td>2.7048</td>
      <td>359.0</td>
      <td>14.9569</td>
      <td>0.0</td>
      <td>1014.55</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
    <tr>
      <th>96435</th>
      <td>2016-09-09 06:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>13.872222</td>
      <td>13.872222</td>
      <td>0.93</td>
      <td>4.7495</td>
      <td>0.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1014.66</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
    <tr>
      <th>96436</th>
      <td>2016-09-09 07:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>16.072222</td>
      <td>16.072222</td>
      <td>0.88</td>
      <td>2.7853</td>
      <td>12.0</td>
      <td>15.7297</td>
      <td>0.0</td>
      <td>1015.25</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
  </tbody>
</table>
<p>10890 rows × 12 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[192]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;Summary&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="s1">&#39;Clear&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[192]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>223</th>
      <td>2006-04-18 07:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>8.688889</td>
      <td>8.688889</td>
      <td>0.93</td>
      <td>1.4329</td>
      <td>290.0</td>
      <td>5.8443</td>
      <td>0.0</td>
      <td>1012.96</td>
      <td>Partly cloudy until night.</td>
    </tr>
    <tr>
      <th>309</th>
      <td>2006-04-20 21:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>12.266667</td>
      <td>12.266667</td>
      <td>0.99</td>
      <td>8.0500</td>
      <td>320.0</td>
      <td>6.1985</td>
      <td>0.0</td>
      <td>1015.76</td>
      <td>Foggy starting overnight continuing until morn...</td>
    </tr>
    <tr>
      <th>337</th>
      <td>2006-04-22 01:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>8.633333</td>
      <td>0.96</td>
      <td>6.4239</td>
      <td>321.0</td>
      <td>3.3649</td>
      <td>0.0</td>
      <td>1017.56</td>
      <td>Foggy starting overnight continuing until morn...</td>
    </tr>
    <tr>
      <th>338</th>
      <td>2006-04-22 02:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>9.861111</td>
      <td>9.861111</td>
      <td>0.96</td>
      <td>3.2361</td>
      <td>319.0</td>
      <td>4.4597</td>
      <td>0.0</td>
      <td>1016.16</td>
      <td>Foggy starting overnight continuing until morn...</td>
    </tr>
    <tr>
      <th>357</th>
      <td>2006-04-22 21:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>12.494444</td>
      <td>12.494444</td>
      <td>0.91</td>
      <td>3.9445</td>
      <td>197.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1015.51</td>
      <td>Foggy starting overnight continuing until morn...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>96432</th>
      <td>2016-09-09 03:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>15.594444</td>
      <td>15.594444</td>
      <td>0.87</td>
      <td>3.2844</td>
      <td>41.0</td>
      <td>15.4399</td>
      <td>0.0</td>
      <td>1014.52</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
    <tr>
      <th>96433</th>
      <td>2016-09-09 04:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>15.011111</td>
      <td>15.011111</td>
      <td>0.93</td>
      <td>3.2039</td>
      <td>341.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1014.37</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
    <tr>
      <th>96434</th>
      <td>2016-09-09 05:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>15.016667</td>
      <td>15.016667</td>
      <td>0.90</td>
      <td>2.7048</td>
      <td>359.0</td>
      <td>14.9569</td>
      <td>0.0</td>
      <td>1014.55</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
    <tr>
      <th>96435</th>
      <td>2016-09-09 06:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>13.872222</td>
      <td>13.872222</td>
      <td>0.93</td>
      <td>4.7495</td>
      <td>0.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1014.66</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
    <tr>
      <th>96436</th>
      <td>2016-09-09 07:00:00.000 +0200</td>
      <td>Clear</td>
      <td>rain</td>
      <td>16.072222</td>
      <td>16.072222</td>
      <td>0.88</td>
      <td>2.7853</td>
      <td>12.0</td>
      <td>15.7297</td>
      <td>0.0</td>
      <td>1015.25</td>
      <td>Partly cloudy starting in the morning.</td>
    </tr>
  </tbody>
</table>
<p>10890 rows × 12 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="The-null--values-of-the-data">The null  values of the data<a class="anchor-link" href="#The-null--values-of-the-data">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[193]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[193]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Formatted Date                0
Summary                       0
Precip Type                 517
Temperature (C)               0
Apparent Temperature (C)      0
Humidity                      0
Wind Speed (km/h)             0
Wind Bearing (degrees)        0
Visibility (km)               0
Loud Cover                    0
Pressure (millibars)          0
Daily Summary                 0
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[194]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">notnull</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[194]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Formatted Date              96453
Summary                     96453
Precip Type                 95936
Temperature (C)             96453
Apparent Temperature (C)    96453
Humidity                    96453
Wind Speed (km/h)           96453
Wind Bearing (degrees)      96453
Visibility (km)             96453
Loud Cover                  96453
Pressure (millibars)        96453
Daily Summary               96453
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Mean-of-Humidity">Mean of Humidity<a class="anchor-link" href="#Mean-of-Humidity">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[195]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[195]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-04-01 00:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.472222</td>
      <td>7.388889</td>
      <td>0.89</td>
      <td>14.1197</td>
      <td>251.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.13</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-04-01 01:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>7.227778</td>
      <td>0.86</td>
      <td>14.2646</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.63</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[196]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">Humidity</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[196]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0.7348989663358906</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[197]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Apparent Temperature (C)&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[197]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>10.855028874166726</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[198]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Wind Speed (km/h)&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[198]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>10.810640140793208</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[199]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Wind Bearing (degrees)&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[199]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>187.50923247592092</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[200]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Visibility (km)&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[200]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>10.347324929237148</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Standard-deviation-of-pressure-in-dataset">Standard deviation of pressure in dataset<a class="anchor-link" href="#Standard-deviation-of-pressure-in-dataset">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[201]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Pressure (millibars)&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">std</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[201]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>116.96990568258147</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Variance-of-'Humidity'in-the-data">Variance of 'Humidity'in the data<a class="anchor-link" href="#Variance-of-'Humidity'in-the-data">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[202]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Humidity&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">var</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[202]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0.03820959171844407</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Find-all-instance-when-'snow'-was-recorded">Find all instance when 'snow' was recorded<a class="anchor-link" href="#Find-all-instance-when-'snow'-was-recorded">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[203]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[203]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-04-01 00:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.472222</td>
      <td>7.388889</td>
      <td>0.89</td>
      <td>14.1197</td>
      <td>251.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.13</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-04-01 01:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>7.227778</td>
      <td>0.86</td>
      <td>14.2646</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.63</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[204]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Precip Type&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[204]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>rain    85224
snow    10712
Name: Precip Type, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[205]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Precip Type&#39;</span><span class="p">]</span> <span class="o">==</span><span class="s1">&#39;snow&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[205]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1562</th>
      <td>2006-12-13 02:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-0.483333</td>
      <td>-4.150000</td>
      <td>1.00</td>
      <td>11.0929</td>
      <td>219.0</td>
      <td>0.4830</td>
      <td>0.0</td>
      <td>1031.56</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1563</th>
      <td>2006-12-13 03:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-0.483333</td>
      <td>-4.061111</td>
      <td>0.96</td>
      <td>10.7387</td>
      <td>200.0</td>
      <td>0.3220</td>
      <td>0.0</td>
      <td>1031.47</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1564</th>
      <td>2006-12-13 04:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-0.922222</td>
      <td>-3.477778</td>
      <td>1.00</td>
      <td>7.0679</td>
      <td>206.0</td>
      <td>0.1610</td>
      <td>0.0</td>
      <td>1031.23</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1565</th>
      <td>2006-12-13 05:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-1.038889</td>
      <td>-4.400000</td>
      <td>1.00</td>
      <td>9.4990</td>
      <td>199.0</td>
      <td>0.1610</td>
      <td>0.0</td>
      <td>1031.41</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1566</th>
      <td>2006-12-13 06:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-1.088889</td>
      <td>-4.438889</td>
      <td>1.00</td>
      <td>9.4346</td>
      <td>219.0</td>
      <td>0.3220</td>
      <td>0.0</td>
      <td>1031.98</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1567</th>
      <td>2006-12-13 07:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-0.994444</td>
      <td>-4.405556</td>
      <td>1.00</td>
      <td>9.7083</td>
      <td>191.0</td>
      <td>0.1610</td>
      <td>0.0</td>
      <td>1032.22</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1568</th>
      <td>2006-12-13 08:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-1.088889</td>
      <td>-4.838889</td>
      <td>0.93</td>
      <td>10.9319</td>
      <td>180.0</td>
      <td>0.3220</td>
      <td>0.0</td>
      <td>1032.88</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1569</th>
      <td>2006-12-13 09:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-1.088889</td>
      <td>-4.411111</td>
      <td>1.00</td>
      <td>9.3541</td>
      <td>209.0</td>
      <td>0.3220</td>
      <td>0.0</td>
      <td>1033.29</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1570</th>
      <td>2006-12-13 10:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-1.077778</td>
      <td>-4.411111</td>
      <td>1.00</td>
      <td>9.4024</td>
      <td>219.0</td>
      <td>0.3059</td>
      <td>0.0</td>
      <td>1033.92</td>
      <td>Foggy throughout the day.</td>
    </tr>
    <tr>
      <th>1571</th>
      <td>2006-12-13 11:00:00.000 +0100</td>
      <td>Foggy</td>
      <td>snow</td>
      <td>-1.061111</td>
      <td>-4.888889</td>
      <td>1.00</td>
      <td>11.2700</td>
      <td>180.0</td>
      <td>0.1610</td>
      <td>0.0</td>
      <td>1034.08</td>
      <td>Foggy throughout the day.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="The-mean-value-of-each-column-against-each-'Daily-Summary'">The mean value of each column against each 'Daily Summary'<a class="anchor-link" href="#The-mean-value-of-each-column-against-each-'Daily-Summary'">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[206]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[206]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-04-01 00:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.472222</td>
      <td>7.388889</td>
      <td>0.89</td>
      <td>14.1197</td>
      <td>251.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.13</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-04-01 01:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>7.227778</td>
      <td>0.86</td>
      <td>14.2646</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.63</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[207]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;Daily Summary&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[207]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
    </tr>
    <tr>
      <th>Daily Summary</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Breezy and foggy starting in the evening.</th>
      <td>4.523843</td>
      <td>0.485880</td>
      <td>0.979583</td>
      <td>21.327133</td>
      <td>137.833333</td>
      <td>6.888117</td>
      <td>0.0</td>
      <td>991.355417</td>
    </tr>
    <tr>
      <th>Breezy and foggy until morning.</th>
      <td>-4.869213</td>
      <td>-10.947222</td>
      <td>0.803750</td>
      <td>21.448554</td>
      <td>257.166667</td>
      <td>7.986942</td>
      <td>0.0</td>
      <td>1014.138750</td>
    </tr>
    <tr>
      <th>Breezy and mostly cloudy overnight.</th>
      <td>3.755787</td>
      <td>-0.340741</td>
      <td>0.733750</td>
      <td>19.908992</td>
      <td>248.833333</td>
      <td>12.492258</td>
      <td>0.0</td>
      <td>1007.213333</td>
    </tr>
    <tr>
      <th>Breezy and partly cloudy in the afternoon.</th>
      <td>28.097917</td>
      <td>27.488657</td>
      <td>0.418333</td>
      <td>16.992208</td>
      <td>223.541667</td>
      <td>11.504792</td>
      <td>0.0</td>
      <td>1005.110000</td>
    </tr>
    <tr>
      <th>Breezy in the morning and foggy in the evening.</th>
      <td>0.743750</td>
      <td>-5.121528</td>
      <td>0.802083</td>
      <td>26.870900</td>
      <td>27.541667</td>
      <td>10.797733</td>
      <td>0.0</td>
      <td>1013.686250</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Partly cloudy until night.</th>
      <td>17.675495</td>
      <td>17.282404</td>
      <td>0.650827</td>
      <td>9.637616</td>
      <td>198.950397</td>
      <td>11.919778</td>
      <td>0.0</td>
      <td>1011.081989</td>
    </tr>
    <tr>
      <th>Rain throughout the day.</th>
      <td>10.128241</td>
      <td>9.285880</td>
      <td>0.892917</td>
      <td>11.803312</td>
      <td>167.625000</td>
      <td>9.109246</td>
      <td>0.0</td>
      <td>1014.335417</td>
    </tr>
    <tr>
      <th>Rain until afternoon.</th>
      <td>11.701157</td>
      <td>11.328009</td>
      <td>0.868333</td>
      <td>11.276708</td>
      <td>69.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>1021.991250</td>
    </tr>
    <tr>
      <th>Rain until morning.</th>
      <td>9.304630</td>
      <td>8.253009</td>
      <td>0.797083</td>
      <td>8.918058</td>
      <td>264.958333</td>
      <td>10.307354</td>
      <td>0.0</td>
      <td>1016.951250</td>
    </tr>
    <tr>
      <th>Windy in the afternoon.</th>
      <td>4.538889</td>
      <td>1.004167</td>
      <td>0.722917</td>
      <td>18.857125</td>
      <td>258.416667</td>
      <td>7.235608</td>
      <td>0.0</td>
      <td>341.752917</td>
    </tr>
  </tbody>
</table>
<p>214 rows × 8 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Visualization">Visualization<a class="anchor-link" href="#Visualization">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[208]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Humidity&#39;</span><span class="p">],</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Temperature (C)&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[208]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x202ac84bd48&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[209]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[209]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Formatted Date</th>
      <th>Summary</th>
      <th>Precip Type</th>
      <th>Temperature (C)</th>
      <th>Apparent Temperature (C)</th>
      <th>Humidity</th>
      <th>Wind Speed (km/h)</th>
      <th>Wind Bearing (degrees)</th>
      <th>Visibility (km)</th>
      <th>Loud Cover</th>
      <th>Pressure (millibars)</th>
      <th>Daily Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-04-01 00:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.472222</td>
      <td>7.388889</td>
      <td>0.89</td>
      <td>14.1197</td>
      <td>251.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.13</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-04-01 01:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.355556</td>
      <td>7.227778</td>
      <td>0.86</td>
      <td>14.2646</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1015.63</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2006-04-01 02:00:00.000 +0200</td>
      <td>Mostly Cloudy</td>
      <td>rain</td>
      <td>9.377778</td>
      <td>9.377778</td>
      <td>0.89</td>
      <td>3.9284</td>
      <td>204.0</td>
      <td>14.9569</td>
      <td>0.0</td>
      <td>1015.94</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2006-04-01 03:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>8.288889</td>
      <td>5.944444</td>
      <td>0.83</td>
      <td>14.1036</td>
      <td>269.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1016.41</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006-04-01 04:00:00.000 +0200</td>
      <td>Mostly Cloudy</td>
      <td>rain</td>
      <td>8.755556</td>
      <td>6.977778</td>
      <td>0.83</td>
      <td>11.0446</td>
      <td>259.0</td>
      <td>15.8263</td>
      <td>0.0</td>
      <td>1016.51</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006-04-01 05:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>9.222222</td>
      <td>7.111111</td>
      <td>0.85</td>
      <td>13.9587</td>
      <td>258.0</td>
      <td>14.9569</td>
      <td>0.0</td>
      <td>1016.66</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2006-04-01 06:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>7.733333</td>
      <td>5.522222</td>
      <td>0.95</td>
      <td>12.3648</td>
      <td>259.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1016.72</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2006-04-01 07:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>8.772222</td>
      <td>6.527778</td>
      <td>0.89</td>
      <td>14.1519</td>
      <td>260.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1016.84</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2006-04-01 08:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>10.822222</td>
      <td>10.822222</td>
      <td>0.82</td>
      <td>11.3183</td>
      <td>259.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1017.37</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2006-04-01 09:00:00.000 +0200</td>
      <td>Partly Cloudy</td>
      <td>rain</td>
      <td>13.772222</td>
      <td>13.772222</td>
      <td>0.72</td>
      <td>12.5258</td>
      <td>279.0</td>
      <td>9.9820</td>
      <td>0.0</td>
      <td>1017.22</td>
      <td>Partly cloudy throughout the day.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[210]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">distplot</span><span class="p">(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Humidity&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[210]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x202aa041948&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWoAAAEGCAYAAABM7t/CAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nO3deXjdZZ338ff3ZN+XJm3aJm2a0tKWFgoNLaVSEFAWHXEBRLYRGSujz6ijzjzO+Iyj4zPXM+o14gKjVkQEBdlEWQRFAQstTRfadF/SNG2TJs2+7zn388c5LYVup+1Zfif5vK6rV87yS873bk4+uXP/7vv+mXMOERHxLl+sCxARkZNTUIuIeJyCWkTE4xTUIiIep6AWEfG4xEh80YKCAldaWhqJLy0iMiqtX7++2TlXeLznIhLUpaWlrFu3LhJfWkRkVDKzfSd6TkMfIiIep6AWEfE4BbWIiMcpqEVEPE5BLSLicQpqERGPU1CLiHicglpExOMU1CIiHheRlYkiIpH0aMX+Yx67ddGUGFQSHepRi4h4nIJaRMTjFNQiIh6noBYR8TgFtYiIxymoRUQ8TkEtIuJxCmoREY9TUIuIeJyCWkTE4xTUIiIep6AWEfE4BbWIiMeFtHuemdUAXcAIMOycK49kUSIi8rbT2eb0vc655ohVIiIix6WhDxERjws1qB3wJzNbb2bLjneAmS0zs3Vmtq6pqSl8FYqIjHGhBvUS59xFwHXA58xs6bsPcM4td86VO+fKCwsLw1qkiMhYFlJQO+cOBj82As8ACyNZlIiIvO2UQW1mGWaWdfg28H5gS6QLExGRgFBmfUwAnjGzw8c/6px7KaJViYjIEacMaudcNXBBFGoREZHj0PQ8ERGPU1CLiHicglpExOMU1CIiHqegFhHxOAW1iIjHKahFRDxOQS0i4nEKahERj1NQi4h4nIJaRMTjFNQiIh6noBYR8TgFtYiIxymoRUQ8TkEtIuJxCmoREY9TUIuIeJyCWkTE4xTUIiIep6AWEfE4BbWIiMcpqEVEPE5BLSLicQpqERGPU1CLiHicglpExOMU1CIiHqegFhHxuJCD2swSzGyDmT0fyYJEROSdTqdH/QVge6QKERGR4wspqM2sGPgA8EBkyxERkXcLtUf9feCfAf+JDjCzZWa2zszWNTU1haU4EREJIajN7INAo3Nu/cmOc84td86VO+fKCwsLw1agiMhYF0qPegnwITOrAX4DXGlmv4poVSIicsQpg9o59y/OuWLnXClwC/CKc+72iFcmIiKA5lGLiHhe4ukc7Jx7DXgtIpWIiMhxqUctIuJxCmoREY9TUIuIeJyCWkTE4xTUIiIep6AWEfE4BbWIiMcpqEVEPE5BLSLicQpqERGPU1CLiHicglpExOMU1CIiHqegFhHxOAW1iIjHKahFRDxOQS0i4nEKahERj1NQi4h4nIJaRMTjFNQiIh6noBYR8TgFtYiIxymoRUQ8TkEtIuJxCmoREY9TUIuIeJyCWkTE4xTUIiIed8qgNrNUM1tjZpVmttXMvhmNwkREJCAxhGMGgCudc91mlgS8YWYvOudWR7g2EREhhKB2zjmgO3g3KfjPRbIoERF5W0hj1GaWYGYbgUbgZedcxXGOWWZm68xsXVNTU7jrFBEZs0IKaufciHNuPlAMLDSzucc5Zrlzrtw5V15YWBjuOkVExqzTmvXhnGsHXgOujUg1IiJyjFBmfRSaWW7wdhpwNbAj0oWJiBzPW/vbaOsdjHUZURXKrI+JwC/NLIFAsD/hnHs+smWJiByr8kA7N/3kTXwGV82awJJzCkjwWazLirhQZn1sAi6MQi0iEgcerdh/3MdvXTQloq/bPzTCl5+spDAzhbz0JF7a2sCOhi4+fdk0zEZ3WIfSoxYRibl7X95FVWM3v/zUQmpbe1mxq4k/bjvEwfZ+Juelxbq8iNISchHxvM21HSx/vZpPLCzh8pmFmBkXT8vHZ7C5riPW5UWcglpEPO9nr1eTmZLIv14/+8hj6cmJTC/MZMvBDgLr8kYvBbWIeFpjVz8vbqnnxgXFZKUmveO5uZNyaO0ZpL6jP0bVRYeCWkQ87TdrDjA04rjjkqnHPDd7UjY+gy0HR/fwh4JaRDxraMTPoxX7uWxGAWWFmcc8n5mSyLSCDLbUje7hD836EJGoOp3pfS9vO0RDZz/f+vAxu1YcMXdyDr/feJAdDV3Mnpgdtjq9RD1qEfEk5xwPvrGXyblpXDlr/AmPm10UCOeVVc3RKi3qFNQi4klvVrewbl8by5aWnXT1YXZaErlpSWw40B7F6qJLQS0invTDv+xmfFYKH7+45JTHFuens3G/glpEJGoqqltYXd3KPZdPJzUp4ZTHT8lLo669j8au0TlNT0EtIp7zw1d2U5CZEvL+ISX56QCjtletoBYRT3n4zRpWVrVwz+VlIfWmASblppHoMzaO0nFqBbWIeMazlQf592e3cvXsCXzy0tKQPy8pwcesiVkKahGRSHDO0djZz32v7ObLT2zk4tJ87rv1QhITTi+eLizJo/JAOyP+0bfwRQteRCRq1uxt5Q+b6znY0UdL9yAjfseI39E3NALApdPH8ePbF4Q85HG0+SW5PLJ6H1WN3ZxblHXSY4+36CbS+2mfDQW1iERce+8g//nCdp5cX0uizyjKSaWsIIOkBB9mMCE7ldkTs8lJS+KFTfVHPu90wnP+lFwANh5oO2VQxxsFtYhE1J6mbm5ZvprWnkHuuXw6RdmpJCeGf9R12rgMslMT2XignY9f7N3e8ZnQGLWIRMyhzn7u/PkanHP8/nNL+Op1syIS0gA+n3FBSS4bD4y+nfQU1CISEZ39Q3zyF2tp7x3kF59cyNzJORF/zfOLc9h9qIv+4Jj3aKGgFpGI+Jffbmb3oS5+fPsC5hVHPqQB5k3OYdjv2F7fGZXXixaNUYtI2D1beZAXNtXzT9ecy9KZhVF73XnFgROKW+o6uHBK3gm3VI036lGLSFgd6uzn3363hQun5PKZpWVRfe1JOankZySzqXZ0jVMrqEUkbJxzfPXpTQwMj/DfN11w2otWzpaZMW9yzqi7MrmGPkQkbB5fe4BXdzbxjb+ZQ1lhZkyGHuZNzuGNquZRdUJRPWoRCYsDrb186/ltLC4bx52LS2NWx9zJOYz4HdtG0QlFBbWInDW/c3zlyUrMjO/edD6+k1yRJdLOD84w2TyKxqkV1CJy1l7f1UTF3la+/sE5FOelx7SWiTmpjMtIHlXj1ApqETkre5t7eHn7IT54/kRuKi+OdTmBE4rFOWOrR21mJWb2qpltN7OtZvaFaBQmIt7XPTDMb9buJy89mf/30XmYxW7I42jzJuewu7GLwWF/rEsJi1B61MPAl51zs4FLgM+Z2ZzIliUiXjcwNMKvV++jb3CEWxdNISs1KdYlHXF+cS5+B3XtfbEuJSxOGdTOuXrn3FvB213AdmBypAsTEe8aGBrhoVU1HGjr5abyEibmpMW6pHe4KLjl6f6WnhhXEh6nNY/azEqBC4GK4zy3DFgGMGXK6NpiUGSsOt486I6+IR5bs5/atl4+fvEU5kVhs6XTNS4zhbKCDPa19sa6lLAI+WSimWUCTwNfdM4dM0HRObfcOVfunCsvLIze2n4RiQ7nHOv3tfGDv+yivqOPWzwa0octmJrH/tZenIv/S3OF1KM2syQCIf1r59xvI1uSiHhNdXM3L287xL6WXkrHpfOxi4oZl5kS67JOqrw0jyfX19LcPUhhlrdrPZVTBrUFTuP+HNjunPte5EsSkZOJ5vX+Gjv7eWFzPbsbu8lOTeSG+ZO4uDQfn0dmd5zMgql5AOxr6Rn9QQ0sAe4ANpvZxuBj/+qc+0PkyhKRWOofGuHeP+/iZyuqSU70cf3cIhaVjSMpypssnY2ygkzSkhLY19pLeWl+rMs5K6cMaufcG4D3f32KSFg0dQ2w7JF1bNjfzoIpeVwzt4jMlPjbv83nM6aOS2d/S/yfUIy//30RiZgdDZ3c/dA6WnoG+MntF9HaMxTrks7K1Px0djR00TswTHoc/rI5LH7+jhGRiNrR0Mknlq9m2O/nyc9cyrVzJ8a6pLM2ZVwGQNxP01NQiwhVjd3c/kAFyYk+nvjM4qhd4zDSivPSSDCjJs4XvsTv3wIiEhY1zT185H9W4hx8+rIyVla1sLKqJdZlhUVSgo/SgnR2NnRxXRz/haCgFhmlTnR1laOn8h1o7eXWn61mxO/4u8vKPDeNLRxXiJlVlM0Lm+tp7RkkPyM5DFVFn4Y+RMaouvY+bn1gNd0Dw3xqyTSKslNjXVJEzCrKAgJj8PFKQS0yBq3f18oN962kvWeIR+5exKRcb22qFE7jMlMoyExhZ0NXrEs5YwpqkTHE7xyPVuznE8sryEhJ4LefvZQLSnJjXVbEzSrKorq5h4E4veCtxqhFxoi6tj6e23SQ/a29vOecAu679UJy0+NzzPZ0zZqYxRtVzexu7GauhzeSOhEFtcgo19DRz6s7G9lS10F6SiLfvfF8PnZRcUwvQBttU/MzSE3ysbOhS0EtIt7R3jvIS1sb2FTbQUqij8tnFrJ0ZiE3lZfEurSoS/AZMydksaOhkxG/IyHOfkkpqEVGmeERPz9dUc33/7wL5+CKmYW8Z0YB6clj+8f9guJcNtV2sLOhkzmT4qtXPba/cyKjTHP3AJ9/bAOr9rRw3qRsrp87kbw4nTscbjMnZJGdmsjamjYFtYjExqbadj798Drae4f47o3nMzQS/1c2CacEn3HR1Dz+urOJ9t7BuDqRqqAWGQXW1rRy1y/WkpuexDOfXcKcSdknXNUXjtV+8ap8aj6v7Wxi/f42rpo1IdblhEzzqEXiXFVjN3f8vILx2Sk8dc+lzJmUHeuSPCs/I5lzCjNZX9OGP46upaigFolj2+s7efjNGkrHZfD4ssUU5YzOZeDhVF6aR3vfEFWN3bEuJWQKapE4tam2nV9X7KMoJ5XfLLvEcxsqedWcidlkpCSyujp+dghUUIvEobf2tfH42gOU5KfzqSXT4urEWKwlJvi4eGoeOxu6aOsZjHU5IVFQi8SZ1dUtPPVWLdPHZ3LXpdNITUqIdUlxZ+G0wMVu19S0xriS0CioReKEc47/ea2KZysPMqsoizsumUpyon6Ez0RuejKzJ2aztqaVoRF/rMs5JX2XReLA4LCf//30Jr7z0k7OL87htkVTSUrQj+/ZuKRsHL2DI2yp64h1KaekedQiHneos5/PP7aBir2tfP7KcxifnYrP4muvCi+aXphBQWYya2tauXBKXqzLOSn9ShbxsJe21HPN91dQWdvOvR+/gC+9/1yFdJiYGfNLctnX0ktH31Csyzkp9ahFPGhvcw/ffnEHL21t4PziHO79+HymF2bGuqyTiscVj3Mn5/Dn7Y1sPejt4Q8FtYhHjPgda/a28rsNdTz9Vi0+n/G+ORNYOqOQiupWKqrjY4ZCPBmflcqE7BQ2e3ycWkEtEkPOOTYeaOfZyoO8sKmexq4B0pISuGVhCSV56WSlJsW6xFFvXrBX3dDR79mVnQpqkShzzrG9vovnNh3kucqD1Lb1keAzzp2QxZWzxjOrKFvT7qLo8PDHi1vquWvJtFiXc1wKapEoqWvv48l1B3iu8iB7mnpI8BnvOaeAL149k86+IS1ciZHDwx8vbIrjoDazB4EPAo3OubmRL0lk9HDOsbq6lV+uquFP2xpwDkoLMrhh/iTOm5RDZkoig8N+hXSMHR7+aOzsZ3y294Y/QulRPwTcBzwc2VJERo/+oRF+t6GOh1bVsKOhi9z0JJYtnU5WaiJ52pfDc84tyubP2xtZuaeZj1xYHOtyjnHKoHbOrTCz0siXIhL/Gjr6eWR1DY9W7Ketd4jZE7P59sfmccP8yaQmJcTlFLaxYGJOKrnpSaysaonPoA6VmS0DlgFMmTIlXF9WxPOcc3z7xR2sqm5hS10HzsHsidl8bEEx08ZlMOKH375VF+sy5SR8ZiwuG8eqqmacc5jHFhWFLaidc8uB5QDl5eXxc+kEkTPQPTDMhv1tvL67mT9srqe2rY+URB+Ly8axeHoB+bqgbNy59JwCXtzSQE1LL9MKMmJdzjto1ofICTxasZ++wREau/pp7h6guXuQtKQEqpu72dPUw4jfkegz3jOjgEXT8jlvUo5OCsaxJdPHAbCyqllBLeJlDR39vLazkRW7m1i1p4X23rf3gPBZYMZGWUEG15xXxMWl+Vw4JZes1CSNPY8C0woymJiTyqo9zdx+ydRYl/MOoUzPewy4Aigws1rg351zP490YSLRMDTiZ/2+Nl7b2cRrOxvZ0dAFQFF2KiV56SwqTaUoJ5WCzBRy05O5Y7G3foAlfMyMS6cX8MqOQ/j9Dp/PO+PUocz6+EQ0ChGJhs7+IXbUd1F5oJ31+9pYWdVM18AwiT6jvDSPr143iyvOLeTcCVk8tubAMZ+vnvPotuSccTz9Vi3bGzo5b1JOrMs5QkMfMio1dQ2wrb6THfWdVDf1sLe5h+rmbpq7375GXl56EucWZfF3l01jyTkF2ldDWHJOAQCrqloU1CLhNDjsZ92+VlZWNbOlrpNt9Z00dQ0ceT4jJZGCzGRKx2VQPjWf8VkpTM5LOxLMrT1DPFdZH6vyxUMmZKdSVpBBxd4WPr20LNblHKGglrhU197HX4PjyiurmukZHCHRZ8yYkMXSGYXMmZRNfXsfRTmppCfrbS6hu7g0n5e2NnhqnFrvYIkLwyN+3trfzis7Gnl1RyM7DwVO+k3OTeO8STnMnJDF9MIMUo6aHlfm8Y32xZsWTsvn8XUH2NXYxayi7FiXAyioJYoOtPayfEU1TV0D9A6O4HAYxqKyfLJTE8lKTSI7LZHkhAR6B4fp7B+muqmbnQ1drK1ppbN/ODBFblwG180tYuaELMZnpXhuFVks6CRn+Cyclg/Amr2tCmoZGzp6h3i2so6n1tdSWfv2VTQSfIYBDlixu+mEn5/oM8oKA/OWr5w1nvqOfi0qkYgqzktjYk4qa/a2cufi0liXAyioJQJG/I43qpp5ct0B/rTtEIPDfmYVZfF/PjCblu5BCjJTSEt+O2yHRvz0D43QPxT4OOx33DB/EpkpiUzKTXvHJvrqOUqkmRkLp+Xz5p4Wz+z7oaCWsKlu6uap9bX89q06Gjr7SUtKYMGUPBZMzWNiTipmRnr+sW+5pAQfSQk+so7aBnhTrbevYSej28Jp+fx+40H2tfRS6oHl5ApqOSu9g8M8X1nPE+sOsG5fGz6Dy2cW8t5Z45ldlEVigi4pJfFn0eFx6ppWBbXEJ+ccm+s6eGxN4LJS3QPDFGamcO15Rcyfkku2Fo5InJtemEl+RjJr9rZyc3lJrMtRUEvoHnlzH5W17aysaqa+o5+kBGPe5BwuLs1nSn66J8byRMLBzLi4NI+KvS2xLgVQUEsI/H7HMxvquPfPu2jtGWRCdgp/c8Ek5hfnvuOkoMhocun0Av649RD7W3qZMi49prUoqOWkNuxv4xvPbaPyQDuTclK5fdFUZk/MUu9ZPCfcM4IumxHY92PF7iZuHxfbXRMV1HJc/UMjfOelnTy4ci+FWSl87+YL6B0cwaeAljFiWkEGk3PTWLGrKeb7Uyuo5RjbDnbyxcc3sOtQN3cunso/XzuLzJREzWGWMcXMWDqzkOcrDzI04icphjOYNHdKjvD7HctX7OHD96+krXeIh+66mP+4YS6ZKfp9LmPT0hkFdA0MU3mgPaZ16CdQgMBudF9+YiOrq1u59rwiFkzN42B7v3rRMqZdOr0An8GKXU2Ul+bHrA71qIXfb6zj2u+vYHNtB9+58Xx+fPtFZKgXLUJOehIXlOSyYndzTOvQT+MY1tE7xB0PVrCptoMp+encXF7C8Ig77iWoRMaqpTMK+dEru2nvHSQ3PTkmNahHPUatqmrm2h+sYEtdB++bM4FPX1ZGfkZs3oQiXrZ0ZgF+B6/ubIxZDQrqMaZ/aIT/+/w2bn2ggrTkBO65fDrvPXc8CR65koWI11xYkkdJfhpPrK2NWQ0K6jFkS10HH75/JQ+8sZc7LpnKC/9wGcV5sV1xJeJ1Pp9x84IS3qxuYV9LT2xqiMmrSlT1D43w7Zd28KH73qCurY+/XTyV2ROzeWZDXaxLE4kLN5YX4zN4Yl1szt/oZOIot2ZvK199ehPVzT2UT83jurkTtT+HyGmamJPGFeeO56n1tfzj1TOjvn2vetSjVGvPIF97ZjM3//RNhvx+fnX3Ij56UbFCWuQM3VxewqHOAf6668SXjosU9ahHmf6hER5aVcP9r1bRMzDMp5ZM4yvXzCQ9WUvARc7GVbPHU5CZzAOv7+XKWeOjujGZgnqU6Ogd4lcV+3jwjb209AwyqyiLa84rYkJ2Kr/bcDDW5YnEvaQEH1+4agb/9vutPLpmP7ctit5GTQrqODbid1TsbeGpdbX8YUs9/UN+rji3kM9ecQ5Vjd2xLk9k1Llt0VT+uPUQ//nCdi47pzBq+1QrqOOIc459Lb2s39fGyqpmXt3ZSFvvEFkpiXzsomJuWzSVOZOyARTUIhHg8xnfvvF8rr13BV95spJffmphVM77hBTUZnYt8AMgAXjAOfdfEa1qjOseGKaho499Lb3saepmT2MPe5q6qWrqpr13CIDc9CTee+54UhJ9zCrKJjnRx8YD7WyM8S5fIqPd5Nw0vnnDeXzpiUo++KPX+d7N87mgJDeir3nKoDazBOB+4H1ALbDWzJ51zm0LdzGDw358Bgk+O+2Beudc8CO44H135Dl4+x74zPCZYYAZZ3RSwDmHc+B3Dn/w6x99f3jET/+Qn76hEfoGR+gbGqE/eLtncJj23iHaegePfGzuHqCho59DnQN0Dwy/47UKMpMpK8xkxvhMJuemM2VcOuOzUrSJv0iMfPSiYsZnpfJPT1Xy0R+v4urZ41lyTgGXTi9gemFG2E80htKjXghUOeeqAczsN8ANQNiD+oJv/om+oZEj9xN8RoLZkZA9UQiHg88CAX44uI3AfUcgeDkSwsH7YZKa5CM9OZGM5ASy05KYV5xDTmoS2WmJ5KcnU5CVQnqyRqhEvOY9Mwp46YtLufflXby87RB/3HqI7NRENnz9/SSEuQ8VSgJMBo5ejlMLLHr3QWa2DFgWvNttZjvPvrwzVgDEdl/CyFC74ovaFUduC1O7Er95xp96wmkkoQT18X43HNOndM4tB5afRlERY2brnHPlsa4j3NSu+KJ2xRcvtyuUlYm1QMlR94sBTcwVEYmSUIJ6LTDDzKaZWTJwC/BsZMsSEZHDTjn04ZwbNrP/BfyRwPS8B51zWyNe2dnxxBBMBKhd8UXtii+ebZe5cE2bEBGRiNDueSIiHqegFhHxuLgNajO71sx2mlmVmX31OM+nmNnjwecrzKw0+lWemRDa9iUz22Zmm8zsL2YWvW28zsKp2nXUcTeamTMzT06VerdQ2mVmNwe/Z1vN7NFo13gmQngfTjGzV81sQ/C9eH0s6jwdZvagmTWa2ZYTPG9m9sNgmzeZ2UXRrvG4Akuh4+sfgZOae4AyIBmoBOa865jPAj8J3r4FeDzWdYexbe8F0oO3/z4e2hZKu4LHZQErgNVAeazrDtP3awawAcgL3h8f67rD1K7lwN8Hb88BamJddwjtWgpcBGw5wfPXAy8SWD9yCVAR65qdc3Hboz6yrN05NwgcXtZ+tBuAXwZvPwVcZdHc6fvMnbJtzrlXnXO9wburCcxt97pQvmcA3wK+A/RHs7izEEq7Pg3c75xrA3DONUa5xjMRSrsckB28nUMcrK9wzq0AWk9yyA3Awy5gNZBrZhOjU92JxWtQH29Z++QTHeOcGwY6gHFRqe7shNK2o91NoAfgdadsl5ldCJQ4556PZmFnKZTv10xgppmtNLPVwd0ovS6Udn0DuN3MaoE/AP8QndIi6nR//qIiXnf7CWVZe0hL3z0o5LrN7HagHLg8ohWFx0nbZWY+4F7gk9EqKExC+X4lEhj+uILAXz+vm9lc55yX96QNpV2fAB5yzv23mS0GHgm2yx/58iLGk7kRrz3qUJa1HznGzBIJ/Gl2sj95vCKkJftmdjXwNeBDzrmBKNV2Nk7VrixgLvCamdUQGB98Ng5OKIb6Xvy9c27IObcX2EkguL0slHbdDTwB4Jx7E0glsLFRPPPklhnxGtShLGt/Fvjb4O0bgVdc8GyBx52ybcEhgp8SCOl4GO+EU7TLOdfhnCtwzpU650oJjL1/yDm3LjblhiyU9+LvCJwAxswKCAyFVEe1ytMXSrv2A1cBmNlsAkEd/Ut0h9ezwJ3B2R+XAB3OufpYFxXzs5lncfb2emAXgTPTXws+9h8Efrgh8KZ5EqgC1gBlsa45jG37M3AI2Bj892ysaw5Hu9517GvEwayPEL9fBnyPwB7um4FbYl1zmNo1B1hJYEbIRuD9sa45hDY9BtQDQwR6z3cD9wD3HPW9uj/Y5s1eeQ9qCbmIiMfF69CHiMiYoaAWEfE4BbWIiMcpqEVEPE5BLSLicQpq8SQz637X/U+a2X1h+tr3mNmdx3m89PCuamZWbmY/DN6+wswuDcdri5yJeF1CLnLGnHM/CeGYdcDhxTZXAN3AqgiWJXJC6lFL3DGzh8zsxqPudwc/XmFmfzWzJ8xsl5n9l5ndZmZrzGyzmU0PHvcNM/tK8PYCM6s0szeBzx31Na8ws+eD+5jfA/yjmW00s8vMbK+ZJQWPyzazmsP3RSJBQS1elRYMxo1mtpHAirhQXAB8AZgH3AHMdM4tBB7g+Lu7/QL4vHNu8fG+mHOuBvgJcK9zbr5z7nUCqyY/EDzkFuBp59xQiPWJnDYFtXhVXzAY5zvn5gNfD/Hz1jrn6l1go6o9wJ+Cj28GSo8+0MxygFzn3F+DDz0S4ms8ANwVvH0XgbAXiRgFtcSjYYLv3eDFIJKPeu7onQT9R933c+w5GeMMtrB0zq0ESs3sciDBOXfcyzqJhIuCWuJRDbAgePsG4IzGh11gP+gOM3tP8KHbTnBoF4FtWI/2MIENftSblohTUEs8+hlwuZmtARYBPWfxte4C7g+eTOw7wTHPAR85fDIx+NivgTwCYS0SUdo9T+QMBGed3OCcuyPWtcjopxiDZlkAAAA3SURBVHnUIqfJzH4EXEdgv2aRiFOPWkTE4zRGLSLicQpqERGPU1CLiHicglpExOMU1CIiHvf/AaR3XkDgvRaAAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[211]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">jointplot</span><span class="p">(</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Humidity&#39;</span><span class="p">],</span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;Temperature (C)&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[211]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;seaborn.axisgrid.JointGrid at 0x202aa19ce48&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[212]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">pairplot</span><span class="p">(</span><span class="n">dataset</span><span class="p">[[</span><span class="s1">&#39;Humidity&#39;</span><span class="p">,</span><span class="s1">&#39;Temperature (C)&#39;</span><span class="p">,</span><span class="s1">&#39;Visibility (km)&#39;</span><span class="p">]])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[212]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;seaborn.axisgrid.PairGrid at 0x202aa538a88&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
