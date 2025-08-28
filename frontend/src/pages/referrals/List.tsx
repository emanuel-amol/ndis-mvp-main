import { useEffect, useState } from 'react'
import { api } from '../../api/client'
import type { Referral } from '../../api/types'

export default function RefList() {
  const [rows, setRows] = useState<Referral[]>([])
  useEffect(() => { api.get<Referral[]>('/referrals/').then(r => setRows(r.data)) }, [])
  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Referrals</h1>
      <ul className="space-y-2">
        {rows.map(r => (
          <li key={r.id} className="p-3 rounded border">
            <div className="font-medium">{r.source}</div>
            <div className="text-sm text-slate-600">{r.notes}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
