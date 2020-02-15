import React from 'react'
import {Link} from "react-router-dom";

class BigImgSection extends React.Component{

    constructor(props){

        super(props);

        this.state={

        }


    }

    render(){

        let navbar=["sale","rent","both"]

        return(

            <div style={{backgroundImage:"url(https://du858p10xk-flywheel.netdna-ssl.com/wp-content/uploads/2017/11/54.jpg)",
                         padding: "88px",backgroundSize :"cover"}}
                         className="bigimg-wraper">

                 <div style={paragraph_style}>
        
        
                     <p>The Home of Home Search℠</p>
        
        
                    <p>With the most complete source of homes for sale & real estate near you</p>
        
        
                </div>
        
                <div>
                    <ul style={list_style}
                        className="bigimg-nav">


                        {navbar.map((iteam)=>{
                          return(
                                <li><button name="salestatuse" value={iteam} onClick={(e)=>this.props.handleData(e)} style={{color:"aquamarine",textDecoration:"none",border:"0px",background:"none"}}>{iteam}</button></li>        
                            )
                        })}
                    </ul>
                </div>
        
                <div style={{display:"flex",margin:"100px 0",justifyContent:"center"}}
                     className="bigimg-serach-bar">

        
                    <div>

                        <Link to={"/apartments"}>
        
                                <button style={btn_style}>
        
                                         go to apartment page
        
                                </button>

                         </Link>
        
                     </div>
        
            </div>
        
        </div>
        

        )
    }

}

let paragraph_style={

    color:"white",
    margin:"40px 0",
    fontSize:"30px"
}

let list_style={

    listStyle: "none",

    display: "flex",

    justifyContent: "space-evenly",

    margin: "20px auto",

    color: "white",
    fontSize:"20px"

}

let input_style={
    border:"1px solid gray",

    borderTopLeftRadius:"2px",

    borderBottomLeftRadius:"2px"

}

let btn_style={

    height:"100%",

    background:"red",

    border:"1px solid gray",

    borderRadius: "25px"

}
export default BigImgSection