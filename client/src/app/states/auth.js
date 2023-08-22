import { createSlice } from '@reduxjs/toolkit'

const initialState = {
	user: null,
	token: null,
	isLogin: false,
	branchSelect: {},
}

const authSlice = createSlice({
	name: 'auth',
	initialState,
	reducers: {
		setCredentials: (state, action) => {
			const { user, token } = action.payload
			state.user = user
			state.token = token
			state.isLogin = true
			state.branchSelect = user.branch[0]
			state.drawerSelect = user.drawer[0]
		},
		logOut: () => initialState,
		isLogin: state => state.isLogin,
		setBranch: (state, action) => {
			state.branchSelect = action.payload
		},
		setDrawer: (state, action) => {
			state.user.drawer = action.payload
		},
	},
})

export const { setCredentials, logOut, isLogin, setBranch, setDrawer } = authSlice.actions

export default authSlice.reducer

export const selectCurrentUser = state => state.auth.user
export const selectCurrentRole = state => state.auth.user.roles
export const selectCurrentLogin = state => state.auth.isLogin
export const selectCurrentToken = state => state.auth.token

export const selectCurrentBranch = state => state.auth?.user?.branch
export const selectBranchSelect = state => state.auth?.branchSelect

export const selectDrawer = state => state.auth?.user?.drawer
