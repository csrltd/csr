


// //blogs
let blogArray = [];
let blogs = document.querySelectorAll('.blog');

blogs.forEach(blog => {
    blogArray.push(blog);

});

for(i=0; i <= blogArray.length; i++) 
{
  
  if(i %2 === 1){
    blogArray[i].classList.add("blog-left")
  }

}