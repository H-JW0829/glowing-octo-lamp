function changeData(flag,data,pageData,page,maxPageSize,length){
    console.log("changeData");
    if(flag){
      if((page) * maxPageSize < length){
        page++;
        let start = (page - 1) * maxPageSize;
        let end = start + maxPageSize;
        if(end >= length){
          pageData = data.slice(start);
        }else{
          pageData = data.slice(start,end);
        }
      }
    }else{
      if(page > 1 ){
        page--;
        let start = (page - 1) * maxPageSize;
        let end = start + maxPageSize;
        pageData = data.slice(start,end);
      }
    }
    return new Array(page,pageData);
}
export{
  changeData
}