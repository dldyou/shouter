const fileloadBtn = $("#fileload-btn")[0];
const serverloadBtn = $("#upload-btn")[0]; // button for server
const fileName = $("#file-name");

function changeFileBox()
{
  fileName.text(fileloadBtn.files[0].name);
}

function uploadFile(){

  var form = fileloadBtn.files[0];
  var formData = new FormData(form[0]);

  const req = $.ajax({
    type:"POST",
    url: "/upload",
    processData: false,
    contentType: false,
    data: formData,
    success: function(rtn){
      console.log("rtn: ", rtn)
    },
    err: function(err){
      console.log("err:", err)
    }
  })
}

$(document).ready(() => {
  fileloadBtn.addEventListener("change", changeFileBox);
  serverloadBtn.addEventListener("click", uploadFile);
});
