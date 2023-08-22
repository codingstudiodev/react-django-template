import { useRoutes } from 'react-router-dom'
// import PrivateRouter from './PrivateRouter'
import PublicRouter from './PublicRouter'

// Layouts
import { DashboardLAyout, LoginLayout } from '../layouts'

import { Login, NotFound } from '@pages'

// Routers
// import operationsRouter from '../pages/operations/router'

const AppRouter = () => {
	const router = useRoutes([
		{
			path: '/',
			element: <DashboardLAyout />,
			children: [
				{
					path: '',
					element: <>Home</>,
				},
				// {
				// 	path: 'operaciones',
				// 	element: <PrivateRouter />,
				// 	children: operationsRouter,
				// },

			],
		},
		{
			path: '/',
			element: <LoginLayout />,
			children: [
				{ path: '', element: <PublicRouter />, children: [{ path: 'login', element: <Login /> }] },
			],
		},
		{
			path: '*',
			element: <NotFound />,
		},
	])

	return router
}

export default AppRouter
