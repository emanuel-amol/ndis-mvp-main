import { useState } from 'react'
import { api } from '../../api/client'
import type { Referral } from '../../api/types'

export default function CreateReferral() {
  const [form, setForm] = useState<Referral>({ source: '', notes: '' })
  const [done, setDone] = useState<Referral | null>(null)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    const { data } = await api.post<Referral>('/referrals/', form)
    setDone(data)
  }

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">New Referral</h1>
      <form onSubmit={submit} className="grid gap-3 max-w-md">
        <input className="border p-2 rounded" placeholder="Source"
          value={form.source} onChange={e => setForm({ ...form, source: e.target.value })}/>
        <textarea className="border p-2 rounded" placeholder="Notes"
          value={form.notes ?? ''} onChange={e => setForm({ ...form, notes: e.target.value })}/>
        <button className="bg-slate-800 text-white px-4 py-2 rounded">Save</button>
      </form>
      {done && <pre className="mt-4 bg-slate-100 p-2 rounded">{JSON.stringify(done, null, 2)}</pre>}
    </div>
  )
}
