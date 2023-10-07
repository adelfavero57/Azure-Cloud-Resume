window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
})


const getVisitCount = () => {
fetch('https://visitorcounteradf.azurewebsites.net/api/vCounter?'
).then(res => res.json()
).then(data => {
    console.log("success");
    output = data.counter;
    console.log(output)
    document.getElementById("counter").innerText = output
}).catch(error => console.log('ERROR')
);
return output
}
