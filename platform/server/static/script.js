const fileloadBtn = $("#fileload-btn")[0];
const serverloadBtn = $("#upload-btn")[0]; // button for server
const fileName = $("#file-name");

function changeFileBox() {
    fileName.text(fileloadBtn.files[0].name);
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
        url: "/upload",
        processData: false,
        contentType: false,
        data: formData,
        success: function(rtn) {
            console.log("rtn: ", rtn)
        },
        err: function(err) {
            console.log("err:", err)
        }
    })
}

$(document).ready(() => {
    fileloadBtn.addEventListener("change", changeFileBox);
    serverloadBtn.addEventListener("click", uploadFile);
});