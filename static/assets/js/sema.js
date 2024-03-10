
let btn = document.getElementById('more-btn');

let links = document.getElementById('more-links');

btn.onclick = () =>{
  if(links.className.includes(' more-show')){
    links.className = links.className.replace(/ more-show/, '')
  } else{
    links.className += ' more-show'
  }
}



