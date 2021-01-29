async function predict(img) {
    let model = await model_promise;
    // model.summary();
    img = await createImageBitmap(img);
    const tensor = tf.browser.fromPixels(img);
    // tensor.print();
    var label = '';
    const r = tensor.slice([0, 0, 0], [-1, -1, 1]);
    const g = tensor.slice([0, 0, 1], [-1, -1, 1]);
    const b = tensor.slice([0, 0, 2], [-1, -1, 1]);
    // rgb to gray based on the composition fron opencv
    // then scale it between 0-1 and invert
    const gray = r.mul(0.299).add(g.mul(0.587)).add(b.mul(0.114)).div(-255).add(1);
    for (var i = 0; i < gray.shape[1]; i+=gray.shape[1]/4) {
        let crop = gray.slice([0, i], [-1, gray.shape[1]/4]);
        crop = crop.expandDims(0);
        let out = model.predictOnBatch(crop);
        out = tf.argMax(out, 1);
        let index = await out.data();
        label += encoding[index[0]];
    }
    console.log('Got U!');
    return label;
}
async function fill(img) {
    label = await predict(img);
    if (website)
        t.contentDocument.querySelector('input[name="ValidCode"]').value = label;
    else
        document.querySelector('input[name="ValidCode"]').value = label;
}



console.log("Script properly injected into page");
const model_promise = tf.loadLayersModel('https://ernestchu.github.io/files/nsysu-captcha-solver/model_tfjs/model.json');
const encoding = '123456789';
const t = document.querySelector('frame[name="qryheader"]');
var website = false; // any website else
if (t) website = true; // grade inquiry

if (website)
    img = t.contentDocument.querySelector('img[name="imgVC"]');
else
    img = document.querySelector('img[name="imgVC"]');

fill(img);
img.onload = () => {
    fill(img);
}
