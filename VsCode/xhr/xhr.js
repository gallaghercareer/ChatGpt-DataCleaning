const getBtn = document.getElementById('get-btn')
const postBtn = document.getElementById('post-btn')

const getData = () => {
const xhr = new XMLHttpRequest();

xhr.open('GET','https://www.balldontlie.io/api/v1/players')

xhr.responseType = 'json'
xhr.onload= () =>{
    let data = xhr.response
    console.log(data)
}
xhr.send()
};

const sendData = () => {};

getBtn.addEventListener('click', getData)
postBtn.addEventListener('click', sendData)


