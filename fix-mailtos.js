String.prototype.reverse = function()
{
  var s = '';
  var i = this.length;

  while (i > 0) {
    s += this.substring(i-1,i);
    i--;
  }

  return s;
}

function fix_mailtos()
{
  anchors = document.getElementsByTagName('a');

  for (var i = 0; i < anchors.length; i++) {
    var item = anchors.item(i);

    if (item.className == 'maddr') {
      var address = item.getAttribute('href').reverse();
      item.setAttribute('href', 'mailto:' + address);

      while (item.hasChildNodes()) {
        item.removeChild(item.firstChild);
      }

      item.appendChild(document.createTextNode(address));
    } else if (item.className == 'mtitle') {
      var address = item.getAttribute('href').reverse();
      item.setAttribute('href', 'mailto:' + address);
    }
  }
}

