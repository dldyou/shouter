const uploadBtn =$("#upload-btn")[0];
uploadBtn.addEventListener("change", handleFiles);

function handleFiles()
{
  console.log($("#upload-btn")[0].files[0]);
  $("#file-name").text(uploadBtn.files[0].name);
  //$("#file-len").text(uploadBtn.files[0].size); 
}