import React, { useState,useEffect } from "react";
import ResearchCard from "../components/ResearchCard";
import Search from "../assets/Search.svg";
import plus from "../assets/plus.svg";
import AddResearch from "../components/AddResearch";
import { GetDataApiCalls } from "../Services";
export default function Home() {
  
  const[researchData,setResearchdata] = useState([]);
  const [filtereddata, setFiltereddata] = useState(researchData);
  useEffect(()=>{
    async function fetchresearchdata(){
       let api_research_data = await GetDataApiCalls('All_Research');
       if(api_research_data.message === 'Failed')
       api_research_data = []
       console.log(api_research_data)
       setResearchdata(api_research_data);
       setFiltereddata(api_research_data);
    }
    fetchresearchdata();
  },[])

  const [show, setShow] = useState(false);
  const SearchData = () => {
    const search = document.getElementById("search").value;
    const filtered = researchData.filter(
      (item) =>
        item.title.toLowerCase().includes(search.toLowerCase()) ||
        item.profName.toLowerCase().includes(search.toLowerCase())
    );
    setFiltereddata(filtered);
  };
  const [SortText, setSortText] = useState("Sort by Departmant");
  const SortData = () => {
    let filter = [...researchData];
    if (SortText === "Sort by Department") {
      filter.sort((a, b) => a.department.localeCompare(b.department));
      setSortText("Sort by Status");
    } else {
      filter.sort((a, b) => b.performance_score - a.performance_score);
      setSortText("Sort by Department");
    }
    setFiltereddata(filter);
  };
  const handleClose = () => setShow(false);
  const handleShow = () => {
    console.log(show);
    setShow(true);
  };
  return (
    <div className="container mt-3">
      {show && <AddResearch handleClose={handleClose} />}
      <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
        <div
          style={{
            display: "flex",
            alignItems: "flex-start",
            gap: "24px",
            justifyContent: "space-between",
            alignSelf: "stretch",
          }}
        >
          <div
            style={{
              display: "flex",
              width: "320px",
              padding: "10px 14px",
              alignItems: "center",
              gap: "8px",
              alignSelf: "stretch",
              justifyContent: "center",
              borderRadius: "var(--radius-medium, 8px)",
              background: "#fff",
            }}
            className="container_Style"
          >
            <img src={Search} alt="Search Icon" style={{ width: "24px" }} />
            <input
              type="text"
              style={{
                border: "none",
                width: "100%",
              }}
              id="search"
              onChange={SearchData}
              placeholder="Search by Research Title or Professor Name"
            />
          </div>
          <div style={{ display: "flex", gap: "12px" }}>
            <div
              style={{
                color: "black",
                display: "flex",
                alignItems: "center",
                gap: "12px",
                background: "#167bff",
                color: "white",
                borderRadius: "8px",
                cursor: "pointer",
              }}
              onClick={SortData}
            >
              <div className="Box">{SortText}</div>
            </div>
            <div
              style={{
                color: "black",
                display: "flex",
                alignItems: "center",
                gap: "12px",
                background: "#167bff",
                color: "white",
                cursor: "pointer",
              }}
              className="Box"
              onClick={handleShow}
            >
              <img src={plus} style={{ width: "24px" }} />
              Add
            </div>
          </div>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "flex-start",
            alignItems: "center",
            flexWrap: "wrap",
            gap: "24px",
          }}
        >
          {filtereddata.map((item, index) => (
            <ResearchCard key={index} data={item} />
          ))}
        </div>
      </div>
    </div>
  );
}
