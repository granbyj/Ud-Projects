const sizePicker = document.getElementById('sizePicker');
const canvas = document.getElementById('pixelCanvas');
let color = document.getElementById("colorPicker");
const heightGlobal = document.getElementById("inputHeight");
const widthGlobal = document.getElementById("inputWidth");


//declare grid before call
function makeGrid(height, width) {
    canvas.innerHTML=""; // Enables grid reset
    for (let r = 0; r < height; r++){
        let row = canvas.insertRow(r);
        for(let c =0 ; c < width; c++){
            let column = row.insertCell(c);
            // Select color input
            //Color when mouse hovers over grid
            column.addEventListener('mousemove',function(event){
            column.style.backgroundColor= color.value;})
        }}};

// Select size input,  call makeGrid
sizePicker.addEventListener('submit', function (event) {
    event.preventDefault();
    const height = heightGlobal.value;
    const width = widthGlobal.value;
    //make inputs pass through grid
    makeGrid(height,width);
   // console.log("Submitted!!");
});