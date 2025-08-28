import { useState } from 'react'
import { api } from '../../api/client'
import type { Participant } from '../../api/types'

export default function Onboard() {
  const [form, setForm] = useState<Participant>({ first_name: '', last_name: '', ndis_number: '' })
  const [created, setCreated] = useState<Participant | null>(null)
  const [err, setErr] = useState<string | null>(null)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setErr(null)
    try {
      const { data } = await api.post<Participant>('/participants/', form)
      setCreated(data)
    } catch (e: any) {
      setErr(e?.response?.data?.detail ?? 'Error')
    }
  }

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Participant Onboarding</h1>
      <form onSubmit={submit} className="grid gap-3 max-w-md">
        <input className="border p-2 rounded" placeholder="First name"
          value={form.first_name} onChange={e => setForm({ ...form, first_name: e.target.value })}/>
        <input className="border p-2 rounded" placeholder="Last name"
          value={form.last_name} onChange={e => setForm({ ...form, last_name: e.target.value })}/>
        <input className="border p-2 rounded" placeholder="NDIS number"
          value={form.ndis_number} onChange={e => setForm({ ...form, ndis_number: e.target.value })}/>
        <button className="bg-slate-800 text-white px-4 py-2 rounded">Create</button>
      </form>
      {err && <p className="text-red-600 mt-3">{err}</p>}
      {created && <pre className="mt-4 bg-slate-100 p-2 rounded">{JSON.stringify(created, null, 2)}</pre>}
    </div>
  )
}
