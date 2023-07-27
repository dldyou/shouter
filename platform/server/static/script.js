const fileloadBtn = $("#fileload-btn")[0];
const serverloadBtn = $("#upload-btn")[0]; // button for server
const fileName = $("#file-name");
const fileLen = $("#file-len");

window.URL = window.URL || window.webkitURL;

function changeTimeForm(sec) {
    sec = Math.floor(sec);
    const h = Math.floor(sec / 3600).toString().padStart(2, '0');
    sec %= 3600;
    const m = Math.floor(sec / 60).toString().padStart(2, '0');
    sec %= 60;
    const s = sec.toString().padStart(2, '0');

    return h + ":" + m + ":" + s;
}

function changeFileSizeForm(bytes) {
    const fsExt = ["B", "KB", "MB", "GB", "TB"];
    let idx = 0;

    while (bytes >= 1024 && idx < 4) {
        bytes /= 1024;
        idx++;
    }

    bytes = Math.floor(bytes * 100) / 100;
    return bytes.toString() + fsExt[idx];
}

function changeFileBox() {
    const file = fileloadBtn.files[0];
    const file_bytes = changeFileSizeForm(file.size);
    const video = document.createElement("video");

    console.log(file_bytes);

    video.src = window.URL.createObjectURL(file);
    video.preload = "metadata";
    video.onloadedmetadata = function() {
        window.URL.revokeObjectURL(video.src);
        if (video.duration < 1) {
            console.log("Invalid Video! Need more than 1s.");
            return;
        }
        fileLen.text(changeTimeForm(video.duration));
    }

    fileName.text(file.name);
}

function uploadFile() {
    const file_length = fileloadBtn.files.length;
    if (file_length == 0) {
        console.log("File Not Found!");
        return;
    }
    const form = fileloadBtn.files[0];
    const formData = new FormData();
    formData.append('file', form);

    const req = $.ajax({
        type: "POST",
        url: "/process",
        processData: false,
        contentType: false,
        data: formData,
        success: function(rtn) {
            console.log("rtn: ", rtn);
            const blob = new Blob([rtn]);
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'subtitle.srt';
            a.click();
        },
        err: function(err) {
            console.log("err:", err);
        }
    });
}

$(document).ready(() => {
    fileloadBtn.addEventListener("change", changeFileBox);
    serverloadBtn.addEventListener("click", uploadFile);
});