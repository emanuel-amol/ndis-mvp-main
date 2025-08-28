import { useEffect, useState } from 'react'
// import { api } from '../../api/client'
// Update the import path below to the correct location of your API client module
import { api } from '../../api/client' // <-- Update this path if necessary
export default function DocList() {
  const [rows, setRows] = useState<any[]>([])
  useEffect(() => { api.get('/documents').then(r => setRows(r.data)) }, [])
  return <pre className="bg-slate-100 p-2 rounded">{JSON.stringify(rows, null, 2)}</pre>
}
