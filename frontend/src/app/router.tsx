import { createBrowserRouter } from 'react-router-dom'
import Layout from './layout'
import Onboard from '../pages/participants/Onboard'
import Validate from '../pages/participants/Validate'
import Profile from '../pages/participants/Profile'
import RefList from '../pages/referrals/List'
import RefCreate from '../pages/referrals/Create'
import CarePlanForm from '../pages/care/PlanForm'
import RiskForm from '../pages/care/RiskForm'
import DocUpload from '../pages/documents/Upload'
import DocList from '../pages/documents/List'
import QuoteCreate from '../pages/quotations/Create'
import Homes from '../pages/sil/Homes'
import Rooms from '../pages/sil/Rooms'
import Calendar from '../pages/schedule/Calendar'
import InvoiceStub from '../pages/invoices/Stub'

export default createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      { path: '/', element: <Onboard /> },
      { path: '/participants/validate', element: <Validate /> },
      { path: '/participants/:id', element: <Profile /> },
      { path: '/referrals', element: <RefList /> },
      { path: '/referrals/new', element: <RefCreate /> },
      { path: '/care/plan', element: <CarePlanForm /> },
      { path: '/care/risk', element: <RiskForm /> },
      { path: '/documents', element: <DocList /> },
      { path: '/documents/upload', element: <DocUpload /> },
      { path: '/quotations/new', element: <QuoteCreate /> },
      { path: '/sil/homes', element: <Homes /> },
      { path: '/sil/rooms', element: <Rooms /> },
      { path: '/schedule', element: <Calendar /> },
      { path: '/invoices', element: <InvoiceStub /> }
    ]
  }
])
