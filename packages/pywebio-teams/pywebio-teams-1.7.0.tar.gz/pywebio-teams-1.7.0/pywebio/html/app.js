let html = `<iframe id="page1" class="pywebio-page" src="https://pywebio-demos.pywebio.online/" frameborder="0"></iframe>`
setTimeout(() => {
    return;
    $('body').append(html);
    console.log('ok')
}, 1000)
