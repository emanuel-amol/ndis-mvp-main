import { useState } from 'react'
// Update the import path below to the correct location of your API client
// For example, if your client is in 'src/api/client.ts', use the following:
import { api } from '../../api/client'
// If the file does not exist, create 'src/api/client.ts' and export your api instance:
// export const api = axios.create({ baseURL: 'http://your-api-url' });

export default function Upload() {
  const [file, setFile] = useState<File | null>(null)
  const [resp, setResp] = useState<any>(null)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!file) return
    const fd = new FormData()
    fd.append('file', file)
    const { data } = await api.post('/documents/upload', fd, { headers: { 'Content-Type': 'multipart/form-data' } })
    setResp(data)
  }

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Upload Document</h1>
      <form onSubmit={submit} className="flex gap-2 items-center">
        <input type="file" onChange={e => setFile(e.target.files?.[0] ?? null)} />
        <button className="bg-slate-800 text-white px-4 py-2 rounded">Upload</button>
      </form>
      {resp && <pre className="mt-4 bg-slate-100 p-2 rounded">{JSON.stringify(resp, null, 2)}</pre>}
    </div>
  )
}
