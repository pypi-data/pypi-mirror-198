
try {
    new Function("import('/reactfiles/frontend/main.33556183.js')")();
} catch (err) {
    var el = document.createElement('script');
    el.src = '/reactfiles/frontend/main.33556183.js';
    el.type = 'module';
    document.body.appendChild(el);
}
