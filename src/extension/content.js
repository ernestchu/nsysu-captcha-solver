console.log("Script properly injected into page");
const encoding = '123456789';
async function main() {
    const model = await tf.loadLayersModel('https://ernestchu.github.io/files/nsysu-captcha-solver/model_tfjs/model.json');
    // model.summary();
    const predict = async () => {
        t = document.querySelector('frame[name="qryheader"]');
        if (t)
            img = t.contentDocument.querySelector('img[name="imgVC"]');
        else
            img = document.querySelector('img[name="imgVC"]');
        var label = '';
        img = await createImageBitmap(img);
        console.log(img);
        const tensor = tf.browser.fromPixels(img);
        // tensor.print();
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
        return label;
    }

    predict().then(label => {
        t = document.querySelector('frame[name="qryheader"]');
        if (t)
            t.contentDocument.querySelector('input[name="ValidCode"]').value = label;
        else
            document.querySelector('input[name="ValidCode"]').value = label;
    }).catch(reason => {
      console.log('catch:', reason);
    });
}
main()
