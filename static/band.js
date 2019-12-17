function setColors() {
  document.getElementById('color1').value = "#f00"
  document.getElementById('color2').value = "#f00"
}

var colorPicker1 = new iro.ColorPicker("#color-picker-container1", {
  // Set the size of the color picker
  width: 180,
  // Set the initial color to pure red
  color: "#f00"
});

var colorPicker2 = new iro.ColorPicker("#color-picker-container2", {
  // Set the size of the color picker
  width: 180,
  // Set the initial color to pure red
  color: "#f00"
});

function onColorChange1(color, changes) {
  document.getElementById('color1').value = color.hexString;
}

function onColorChange2(color, changes) {
  document.getElementById('color2').value = color.hexString;
}

colorPicker1.on('color:change', onColorChange1);
colorPicker2.on('color:change', onColorChange2);
