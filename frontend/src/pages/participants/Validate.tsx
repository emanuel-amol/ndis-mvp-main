import { useEffect, useState } from 'react'
import { api } from '../../api/client'
import type { Participant } from '../../api/types'

export default function Validate() {
  const [rows, setRows] = useState<Participant[]>([])
  useEffect(() => { api.get<Participant[]>('/participants/').then(r => setRows(r.data)) }, [])
  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Participants</h1>
      <ul className="space-y-2">
        {rows.map(p => (
          <li key={p.id} className="p-3 rounded border">
            {p.first_name} {p.last_name} — {p.ndis_number}
          </li>
        ))}
      </ul>
    </div>
  )
}
