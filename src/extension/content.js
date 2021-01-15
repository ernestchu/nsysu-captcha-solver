console.log("Script properly injected into page");

t = document.querySelector('frame[name="qryheader"]');
if (t)
    t.contentDocument.querySelector('input[name="ValidCode"]').value = "test";
else
    box = document.querySelector('input[name="ValidCode"]').value = "test";
