import { useState } from 'react'
import './App.css'
import Navbar from './Navbar'
import { notes } from './notes'

type Note = {title: string, content: string}

function Note({title, content}: Note) {


  return (
          <>
          <div className='note'>
            <h1>
              {title}
            </h1>
            <p>{content}</p>
            </div>
          </>

  )
}

export default function App() {
  const [usernotes, setNotes] = useState(notes)
  const [addingNote, setAddingNote] = useState(false)
  const [form, setForm] = useState({title: "", content: ""})

  return (
    <>
    
      <Navbar></Navbar>
      
      <div id="notes-container">
        {usernotes.map((x)=> 
        <>
        

          <Note key={x.id} title={x.title} content={x.content}></Note>
       
        </>
      )}
      </div>

      <div id='add-note' onClick={()=>setAddingNote(!addingNote)}>
          +
      </div>

      {addingNote &&
        <div className='overlay'>
          
            <div className='form'>
            <Note title={form.title} content={form.content}></Note>
              <input type="text"
                      value={form.title}
                      onChange={(e)=>setForm({...form, title: e.target.value})}
              />
              <textarea 
                value={form.content}
                onChange={(e)=>setForm({...form, content:e.target.value  })}
              ></textarea>
            </div>
        </div>
      }

    

    </>
  )
}