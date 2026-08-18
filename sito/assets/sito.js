/* Regina Coolors — comportamenti del sito (nessuna libreria esterna) */
(function () {
  'use strict';

  /* menu mobile ------------------------------------------------------------ */
  var apri = document.querySelector('.apri-menu');
  var menu = document.getElementById('menu-mobile');
  if (apri && menu) {
    var chiudi = menu.querySelector('.chiudi-menu');
    var mostra = function (si) {
      menu.classList.toggle('aperto', si);
      document.body.style.overflow = si ? 'hidden' : '';
      apri.setAttribute('aria-expanded', si ? 'true' : 'false');
    };
    apri.addEventListener('click', function () { mostra(!menu.classList.contains('aperto')); });
    if (chiudi) chiudi.addEventListener('click', function () { mostra(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') mostra(false); });
  }

  /* comparsa dei blocchi allo scorrimento ---------------------------------- */
  var daMostrare = document.querySelectorAll('.appari');
  if ('IntersectionObserver' in window && daMostrare.length) {
    var osservatore = new IntersectionObserver(function (voci) {
      voci.forEach(function (v) {
        if (v.isIntersecting) { v.target.classList.add('visto'); osservatore.unobserve(v.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    daMostrare.forEach(function (n) { osservatore.observe(n); });
  } else {
    daMostrare.forEach(function (n) { n.classList.add('visto'); });
  }

  /* modulo contatti: compone il messaggio e lo manda su WhatsApp o via mail - */
  var modulo = document.getElementById('modulo-contatti');
  if (modulo) {
    var componi = function () {
      var d = new FormData(modulo);
      var righe = [
        'Ciao Regina! Sono ' + (d.get('nome') || '').trim() + '.',
        '',
        'Esperienza: ' + (d.get('esperienza') || 'da definire'),
        'Persone: ' + (d.get('persone') || 'non indicato'),
        'Periodo: ' + (d.get('periodo') || 'non indicato'),
        '',
        (d.get('messaggio') || '').trim(),
        '',
        'I miei contatti: ' + (d.get('email') || '') + ' ' + (d.get('telefono') || '')
      ];
      return righe.join('\n');
    };
    var valido = function () {
      if (modulo.reportValidity && !modulo.reportValidity()) return false;
      return true;
    };
    var bWa = document.getElementById('invia-whatsapp');
    var bMail = document.getElementById('invia-mail');
    if (bWa) bWa.addEventListener('click', function () {
      if (!valido()) return;
      window.open('https://wa.me/' + modulo.dataset.wa + '?text=' + encodeURIComponent(componi()), '_blank', 'noopener');
    });
    if (bMail) bMail.addEventListener('click', function () {
      if (!valido()) return;
      window.location.href = 'mailto:' + modulo.dataset.mail +
        '?subject=' + encodeURIComponent('Richiesta info · Regina Coolors') +
        '&body=' + encodeURIComponent(componi());
    });
  }

  /* precompila l'esperienza se arrivo da un bottone "prenota" --------------- */
  var scelta = new URLSearchParams(location.search).get('exp');
  if (scelta) {
    var sel = document.querySelector('#modulo-contatti [name="esperienza"]');
    if (sel) {
      Array.prototype.forEach.call(sel.options, function (o) {
        if (o.value.toLowerCase() === scelta.toLowerCase()) sel.value = o.value;
      });
    }
  }
})();
