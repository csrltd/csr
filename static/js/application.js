const generalDiv = document.querySelector('#general')
const documentsDiv = document.querySelector('#documents')
const referenceDiv = document.querySelector('#reference')

const generalBtn = document.querySelector('#btnGeneral')
const documentsBtn = document.querySelector('#btnDocuments')


generalBtn.addEventListener('click', (event)=>{
   event.preventDefault()
    generalDiv.style.display='none'
    documentsDiv.style.display='flex'
    
})
documentsBtn.addEventListener('click', (event)=>{
    event.preventDefault()
    documentsDiv.style.display='none'
    referenceDiv.style.display='flex'
     
 })
