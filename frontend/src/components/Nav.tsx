import { Link, NavLink } from 'react-router-dom'

const LinkItem = ({ to, children }: { to: string; children: React.ReactNode }) => (
  <NavLink to={to} className={({isActive}) => `px-3 py-2 rounded-md ${isActive ? 'bg-slate-800 text-white' : 'hover:bg-slate-200'}`}>
    {children}
  </NavLink>
)

export function Nav() {
  return (
    <header className="bg-white shadow">
      <div className="max-w-5xl mx-auto px-6 py-4 flex items-center gap-4">
        <Link to="/" className="font-semibold">NDIS</Link>
        <nav className="flex flex-wrap gap-1">
          <LinkItem to="/">Onboard</LinkItem>
          <LinkItem to="/participants/validate">Validate</LinkItem>
          <LinkItem to="/referrals">Referrals</LinkItem>
          <LinkItem to="/care/plan">Care</LinkItem>
          <LinkItem to="/care/risk">Risk</LinkItem>
          <LinkItem to="/documents">Docs</LinkItem>
          <LinkItem to="/quotations/new">Quote</LinkItem>
          <LinkItem to="/sil/homes">Homes</LinkItem>
          <LinkItem to="/sil/rooms">Rooms</LinkItem>
          <LinkItem to="/schedule">Schedule</LinkItem>
          <LinkItem to="/invoices">Invoices</LinkItem>
        </nav>
      </div>
    </header>
  )
}
