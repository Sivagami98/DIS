function submitContactDetails(){
    console.log("contactuspage")
    let firstName = document.getElementById("firstName");
    let lastName = document.getElementById("lastName");
    let email = document.getElementById("email");
    let contactNo = document.getElementById("contactNo");
    let eventType = document.getElementById("eventType");
    let contactType = document.getElementById("contactType");
    let eventDate = document.getElementById("eventDate");

  if (firstName.value == "" || lastName.value == "" || email.value=="" || contactNo.value=="" || eventType.value =="" || contactType.value=="" ||eventDate.value=="") {
    alert("Ensure you input a value in both fields!");
  } else {
    // perform operation with form input
    alert("This form has been successfully submitted!");
  
    
    console.log(`This form has a firstName of ${firstName.value} and lastName of ${lastName.value} and email of ${email.value} and contactNo of ${contactNo.value}
      and eventType of ${eventType.value} and contactType of ${contactType.value} and eventDate of ${eventDate.value}`);
    

  
    firstName.value = "";
    lastName.value = "";
    email.value= "";
    contactNo.value= "";
    eventType.value= "";
    contactType.value= "";
    eventDate.value= "";
  }
}


   
