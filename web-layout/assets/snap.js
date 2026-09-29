/* House web layout: pad every grid item (and any .hw-snap block) so it ends on a row line.
   Row lines fall every --hw-pitch from the top of the nearest .hw-container.
   Not for Canvas (no scripts); there, headings sit in a .hw-rows-N cell instead. */
(function () {
  function px(el, name) {
    var probe = document.createElement('div');
    probe.style.cssText = 'position:absolute;visibility:hidden;height:var(' + name + ')';
    el.appendChild(probe);
    var v = probe.getBoundingClientRect().height;
    el.removeChild(probe);
    return v;
  }
  function snap() {
    document.querySelectorAll('.hw-container').forEach(function (box) {
      var pitch = px(box, '--hw-pitch'), gutter = px(box, '--hw-gutter');
      box.querySelectorAll('.hw-grid > *, .hw-snap').forEach(function (el) {
        el.style.paddingBottom = '0px';
        var h = el.getBoundingClientRect().height + gutter;
        var extra = Math.ceil(h / pitch - 0.001) * pitch - h;
        el.style.paddingBottom = extra.toFixed(2) + 'px';
      });
    });
  }
  var t;
  function later() { clearTimeout(t); t = setTimeout(snap, 50); }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(snap);
  window.addEventListener('load', snap);
  window.addEventListener('resize', later);
})();
