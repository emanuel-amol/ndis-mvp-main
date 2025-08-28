export interface Participant {
  id?: number
  first_name: string
  last_name: string
  ndis_number: string
  dob?: string | null
}

export interface Referral {
  id?: number
  participant_id?: number | null
  source: string
  notes?: string | null
}

export interface CarePlan {
  id?: number
  participant_id: number
  goals?: string | null
  supports?: string | null
}

export interface RiskAssessment {
  id?: number
  participant_id: number
  risks?: string | null
  mitigations?: string | null
}

export interface Document {
  id?: number
  participant_id?: number | null
  filename: string
  url: string
}

export interface Home { id?: number; name: string; address?: string | null }
export interface Room { id?: number; home_id: number; name: string }
export interface Quotation { id?: number; participant_id: number; summary?: string | null }
export interface Invoice { id?: number; participant_id: number; amount_cents: number; status?: string }
