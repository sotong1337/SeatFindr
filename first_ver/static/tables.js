function changeColor(element, table_) {
    console.log(element.textContent);
    // Get the text content of the provided element.
    if (element.textContent == "Cleaned") {
        table_.style.backgroundColor = "yellowgreen";
    }
    else if (element.textContent == "Unclean") {
        table_.style.backgroundColor = "red";
    }
}
  
// Get all the elements from the DOM with the test CSS class. You can also
// use the getElementsByClassName if you prefer.
const tables = document.querySelectorAll('.table');
const elements = document.querySelectorAll('.table p');

// Iterate over all the element and for each element call the changeColor method.
var i;
for (i = 0; i < tables.length; i++) {
    changeColor(elements[i], tables[i]);
}