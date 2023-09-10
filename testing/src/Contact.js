import React,{useState}from 'react'


const Contact = () => {

  const [email,setEmail] = useState("")
  const [password,setPassword] = useState("")

  const [allEntry,setAllEntry] = useState([])

  const formSubmit = (e) =>{
    e.preventDefault();
    const newEntry = {email : email,password : password};
    setAllEntry(newEntry)
    console.log(allEntry)
  }

  return (
    <div className='contact_page'>
      <div className='container col-8 mx-auto'>
        <h1 className='text-center pb-3 pt-4'>Contact Us</h1>
        <form onSubmit={formSubmit}>
          <div className="mb-3">
            <label htmlFor="exampleInputEmail1" className="form-label">Email</label>
            <input type="email" name='email' value={email} onChange={(e) =>setEmail(e.target.value)} className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" required />
          </div>
          <div className="mb-3">
            <label htmlFor="exampleInputpassword" className="form-label">Password</label>
            <input type="text" name='password' value={password} onChange={(e) => setPassword(e.target.value)} className="form-control" id="exampleInputpassword" required />
          </div>
          <button type="submit" className="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  )
}

export default Contact
