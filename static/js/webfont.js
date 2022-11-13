WebFontConfig = {
  google: {
    families: [
      "Nunito+Sans:300,400,500,700,900",
      "Quicksand:300,400,500,700",
    ],
  },
};

function font() {
  var wf = document.createElement("script");

  wf.src =
    ("https:" == document.location.protocol ? "https" : "http") +
    "://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js";
  wf.type = "text/javascript";
  wf.async = "true";

  var s = document.getElementsByTagName("script")[0];

  s.parentNode.insertBefore(wf, s);
}

font();