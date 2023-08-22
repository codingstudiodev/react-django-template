import PropTypes from 'prop-types'
import { Outlet, useLocation, Navigate } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { selectCurrentUser } from '../app/states/auth'
import ROUTES from '../helpers/routes'

const PrivateRouter = ({ allowedRoles }) => {
	const location = useLocation()
	const user = useSelector(selectCurrentUser)

	const hasRole = allowedRoles => allowedRoles?.includes(user?.roles)

	if (!user) {
		return <Navigate to={ROUTES.login} state={{ from: location }} replace />
	} else {
		if (allowedRoles && !hasRole(allowedRoles)) {
			return <Navigate to={ROUTES.home} state={{ from: location }} replace />
			// return <Navigate to={'/unauthorized'} state={{ from: location }} replace />
		}
		return <Outlet />
	}
}

PrivateRouter.propTypes = {
	allowedRoles: PropTypes.arrayOf(PropTypes.string),
	drawer: PropTypes.bool,
}

export default PrivateRouter
