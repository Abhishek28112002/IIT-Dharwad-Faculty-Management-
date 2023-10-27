export const SetItemLocalStorage=(type,data)=>{
    localStorage.setItem(type,JSON.stringify(data))
}
export const GetItemLocalStorage=(type)=>{
   let data= localStorage.getItem(type);
   return data;
}
let url='http://12323123';
export const PostDataApiCalls=async(endpoint,data)=>{
   try{
       let response=await fetch(url+endpoint,{
        method:'POST',
        headers:{content:'json/application'},
        body:JSON.stringify(data)
       })
       response=await response.json();
       return response;
   }
   catch(error)
   {
    console.log(error);
    return({message:'Failed'});
   }
}
export const GetDataApiCalls=async(endpoint)=>{
    try{
        let response=await fetch(url+endpoint)
        response=await response.json();
        return response;
    }
    catch(error)
    {
     console.log(error);
     return({message:'Failed'});
    }
 }