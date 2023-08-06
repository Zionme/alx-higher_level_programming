// script that updates the text color of the <header> element to red
// (#FF0000) when the user clicks on the tag DIV#red_header
const tag = document.querySelector('div#red_header');
tag.addEventListener('click', updateColor);
function updateColor () {
  tag.style.color = '#FF0000';
}
