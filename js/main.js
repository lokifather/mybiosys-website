(function () {
  var ls = document.querySelector('.langsel');
  if (ls) { document.addEventListener('click', function (e) { if (!ls.contains(e.target)) ls.removeAttribute('open'); }); document.addEventListener('keydown', function (e) { if (e.key === 'Escape') ls.removeAttribute('open'); }); }

  // Services dropdown
  var dd = document.querySelector('.dd');
  if (dd) {
    var ddb = dd.querySelector('button');
    ddb.addEventListener('click', function (e) {
      e.stopPropagation();
      var o = dd.classList.toggle('open'); ddb.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
    document.addEventListener('click', function (e) { if (!dd.contains(e.target)) { dd.classList.remove('open'); ddb.setAttribute('aria-expanded', 'false'); } });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { dd.classList.remove('open'); ddb.setAttribute('aria-expanded', 'false'); } });
  }

  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Traceability map: highlight the chain connected to a node
  var map = document.querySelector('.tmap');
  if (map) {
    var edges = JSON.parse(map.getAttribute('data-edges'));
    var def = map.getAttribute('data-default');
    var selected = def;
    var nodes = map.querySelectorAll('.node');
    var paths = map.querySelectorAll('.edge');

    function walk(start, dir) {
      var seen = {}; var q = [start];
      while (q.length) {
        var cur = q.shift();
        edges.forEach(function (e) {
          var from = dir === 'down' ? e[0] : e[1];
          var to = dir === 'down' ? e[1] : e[0];
          if (from === cur && !seen[to]) { seen[to] = true; q.push(to); }
        });
      }
      return seen;
    }
    function show(id) {
      var set = {}; set[id] = true;
      var up = walk(id, 'up'), down = walk(id, 'down');
      Object.keys(up).forEach(function (k) { set[k] = true; });
      Object.keys(down).forEach(function (k) { set[k] = true; });
      nodes.forEach(function (n) { n.classList.toggle('on', !!set[n.getAttribute('data-id')]); });
      paths.forEach(function (p) {
        p.classList.toggle('on', !!set[p.getAttribute('data-from')] && !!set[p.getAttribute('data-to')]);
      });
      map.classList.add('has-sel');
    }
    show(selected);
    nodes.forEach(function (n) {
      var id = n.getAttribute('data-id');
      n.addEventListener('mouseenter', function () { show(id); });
      n.addEventListener('mouseleave', function () { show(selected); });
      n.addEventListener('focus', function () { show(id); });
      n.addEventListener('click', function () { selected = id; show(id); });
      n.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); selected = id; show(id); }
      });
    });
  }

  // Contact form
  var form = document.querySelector('form.contact');
  if (form) {
    var params = new URLSearchParams(location.search);
    var topic = params.get('topic');
    if (topic && form.elements.topic) {
      Array.prototype.forEach.call(form.elements.topic.options, function (o) {
        if (o.value === topic) form.elements.topic.value = topic;
      });
    }
    var status = form.querySelector('.status');
    function say(msg, cls) { status.textContent = msg; status.className = 'status ' + (cls || ''); }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.elements.website && form.elements.website.value) return; // honeypot
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var d = {
        name: form.elements.name.value.trim(),
        company: form.elements.company.value.trim(),
        email: form.elements.email.value.trim(),
        topic: form.elements.topic.options[form.elements.topic.selectedIndex].text,
        message: form.elements.message.value.trim()
      };
      var endpoint = form.getAttribute('data-endpoint');
      if (endpoint) {
        say(form.getAttribute('data-msg-sending'), '');
        fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({
            access_key: form.getAttribute('data-key'),
            subject: '[mybiosys] ' + d.topic + ' - ' + d.company + ' ' + d.name,
            from_name: 'mybiosys.com',
            name: d.name, company: d.company, email: d.email, topic: d.topic, message: d.message
          })
        }).then(function (r) {
          if (!r.ok) throw new Error('bad');
          return r.json();
        }).then(function (res) {
          if (!res || res.success === false) throw new Error('bad');
          form.reset();
          say(form.getAttribute('data-msg-ok'), 'ok');
        }).catch(function () { say(form.getAttribute('data-msg-err'), 'err'); });
      } else {
        var to = form.getAttribute('data-mailto');
        var subject = '[' + d.topic + '] ' + d.company + ' ' + d.name;
        var body = d.message + '\n\n---\n' + d.name + '\n' + d.company + '\n' + d.email;
        location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
        say(form.getAttribute('data-msg-mail'), 'ok');
      }
    });
  }
})();

// News filter
(function () {
  var chips = document.querySelectorAll('.chip');
  if (!chips.length) return;
  var items = document.querySelectorAll('.news-item');
  chips.forEach(function (ch) {
    ch.addEventListener('click', function () {
      var r = ch.getAttribute('data-r');
      chips.forEach(function (c) { c.classList.toggle('on', c === ch); });
      items.forEach(function (it) { it.hidden = !(r === 'all' || it.getAttribute('data-region') === r); });
    });
  });
})();
