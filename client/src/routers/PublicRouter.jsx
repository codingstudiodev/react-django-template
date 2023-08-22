import PropTypes from 'prop-types'
import { Outlet, useLocation, Navigate } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { selectCurrentUser } from '../app/states/auth'

const PublicRouter = () => {
	const location = useLocation()
	const user = useSelector(selectCurrentUser)

	if (user) {
		return <Navigate to={'/'} />
	}
	return <Outlet context={{ from: location }} />
}

PublicRouter.propTypes = {
	allowedRoles: PropTypes.arrayOf(PropTypes.string),
	drawer: PropTypes.bool,
}

export default PublicRouter
