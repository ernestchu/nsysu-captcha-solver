let net;
const webcamElement = document.getElementById('webcam');

async function app() {
    console.log('Loadgin mobilenet...');

    net = await mobilenet.load();
    console.log('Successfully loaded model');

    const webcam = await tf.data.webcam(webcamElement);
    while (true) {
        const img = await webcam.capture();
        const result = await net.classify(img);

        document.getElementById('console').innerText = `
            prediction: ${result[0].className}\n
            probability: ${result[0].probability}
        `;
        img.dispose();
        await tf.nextFrame();
    }
}

app();
