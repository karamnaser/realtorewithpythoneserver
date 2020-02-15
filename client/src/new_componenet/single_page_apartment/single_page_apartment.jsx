import React from 'react'
import GallarymenDetails from '../gallary/gallarydetails';
import GallaryImg from '../gallary/gallary_img';
import Heart from '../gallary/heart'
import './singlepageapartmentmobilecss.css'
import rightarrowicon from '../../icons/right-arrow.png'
import leftarrowicon from '../../icons/left-arrow.png'
import {getapartments,getApartmentImgs} from '../../server/api'

 class SinglePageApartment extends React.Component{
    constructor(props){
      
    super(props)

    this.state={
    apartment: [] ,
    imeges:[],
    id : this.props.match.params.id,
    index : 0 ,
    target : document.getElementsByClassName("apartments-imges")
    }
  }


  componentDidMount(){
    getapartments(`?id=${this.state.id}`)
    .then(apartment=>{
      this.setState({apartment:apartment},()=>console.log(this.state.apartment))
    })
    getApartmentImgs(this.state.id)
    .then(imegs=>{
      this.setState({imeges:imegs},()=>console.log(this.state.imeges))
    })
  }


display_heart_on_hover(event) {

  let target_elemnt=event.target;

      target_elemnt.style.opacity="1";
      
}

disaple_heart_on_leave(event) {

  let target_elemnt=event.target;

      target_elemnt.style.opacity="0";

}
getapartmentDiscreption(aprtment){

  var apartment_discription="";

  if(aprtment["number_of_beds"]){

      var apartments_bed=aprtment["number_of_beds"]+" beds ";
      apartment_discription+=apartments_bed;

  }


  if(aprtment["number_of_rooms"]){

      var apartments_rooms=aprtment["number_of_rooms"]+" room ";
      apartment_discription+=apartments_rooms;

  }

  if(aprtment["sqft"]){

      var apartments_size=aprtment["sqft"]+" sqft"+"\n";
      apartment_discription+=apartments_size;

  }

  if(aprtment["address"]){

      var apartments_addres=aprtment["address"];
      apartment_discription+= apartments_addres

  }

  return apartment_discription;
  
}


    render(){

    return (

     
        
        <div  className="apartment  mt-2  position-relative w-50">

              {this.state.apartment.length>0 ?

              <div style={{boxShadow:"0px 0px 0px 1px"}} className="shadow-div">

                    <GallarymenDetails header={this.state.apartment[0]["description"]}/>

                    <GallaryImg src={`http://127.0.0.1:5000/images/apartment/${this.state.apartment[0]["main_img"]}`}/>

                        
                   <GallarymenDetails header={this.getapartmentDiscreption(this.state.apartment[0])}/>


                   <Heart onMouseOver={this.display_heart_on_hover.bind(this)}
                          onMouseLeave={this.disaple_heart_on_leave.bind(this)}/>


                    <p className="apartment-price">{this.state.apartment[0]["price"] &&"$"+this.state.apartment[0]["price"]}</p>


                    
                    {this.state.imeges.length>0 && this.state.imeges[0]["imeges"].map((iteam,i)=>{
                        
                        return(

                                 <div className="img-wraper position-absolute">
                                

                                        <img className="apartments-imges" src={`http://127.0.0.1:5000/images/apartment/${iteam}`}/>

            
                                </div>
                                

                             )

                            })
                            }
                            <div id="map-container-google-1" class="z-depth-1-half map-container" style={{height: "500px"}}>
                
                                  <iframe src={`https://maps.google.com/maps?q=${this.state.apartment["address"]}&t=&z=13&ie=UTF8&iwloc=&output=embed`} frameborder="0"
                                          style={{border:"0px"}} allowfullscreen></iframe>
                        
                            </div>

                  
                    
                </div>
                :"loading"}

                <button  className="right-arrow" 
                          onClick={()=>{

                            if(this.state.index>this.state.target.length-1){

                              this.state.index=0

                              let counter=0

                              while(counter<=this.state.target.length-1){

                                  this.state.target[counter].style.left="2000px"
                                  counter++

                              }

                              return

                            }
                            
                              this.state.target[this.state.index].style.left="1px"
                              

                            this.state.index++
                          }
                        }> 
                      
         
                        <img src={rightarrowicon}/>
                                     
                                     
                </button>
                    

                <button className="left-arrow" 
                        onClick={()=>{
                                    
                          if(this.state.index>this.state.target.length-1){

                            this.state.index=0

                            let counter=0

                            while(counter<=this.state.target.length-1){

                                this.state.target[counter].style.left="2000px"
                                counter++

                            }

                            return
                          }
                        
                          this.state.target[this.state.index].style.left="1px";

                          this.state.index++
                        }
                      }>  


                        <img src={leftarrowicon}/>

                        

                </button>
                        
         </div>

    )

}
 }
 

export default SinglePageApartment;