import { createApi } from '@reduxjs/toolkit/query/react'
import { setCredentials, logOut } from '../app/states/auth'
import axios from 'axios'

export const baseUrl = 'http://127.0.0.1:8000'

const axiosBaseQuery =
	({ baseUrl = '', prepareHeaders }) =>
	async ({ url, params, method, body, headers = {} }, api) => {
		try {
			const result = await axios({
				url: baseUrl + url,
				method,
				...(params && { params }),
				...(body && { data: body }),
				...(headers && { headers: prepareHeaders(headers, api) }),

				responseType: 'json',
			})
			return { data: result.data }
		} catch (err) {
			return {
				error: {
					status: err.response?.status,
					data: err.response?.data || err.message,
				},
			}
		}
	}

const baseQuery = axiosBaseQuery({
	baseUrl: `${baseUrl}/v1`,
	credentials: 'include',
	prepareHeaders: (headers, { getState }) => {
		const token = getState().auth?.token
		if (token) {
			headers.authorization = `Bearer ${token.access}`
		}
		return headers
	},
})

export const baseQueryWithReauth = async (args, api, extraOptions) => {
	let result = await baseQuery(args, api, extraOptions)

	if (result?.error?.status === 401) {
		const refreshResult = await baseQuery(
			{
				url: '/auth/refresh/',
				method: 'POST',
				body: { refresh: api.getState().auth.token?.refresh },
			},
			api,
			extraOptions
		)
		if (refreshResult.data) {
			const user = api.getState().auth.user
			api.dispatch(
				setCredentials({
					user,
					accessToken: {
						access: refreshResult.data.access,
						refresh: refreshResult.data.refresh,
					},
				})
			)
			result = await baseQuery(args, api, extraOptions)
		} else {
			api.dispatch(logOut())
		}
	}

	return result
}

export const apiSliceWithRefresh = createApi({
	baseQuery: baseQueryWithReauth,
	reducerPath: 'apiSliceWithRefresh',
	keepUnusedDataFor: 0,
	refetchOnMountOrArgChange: true,
	endpoints: () => ({}),
})

export const apiSlice = createApi({
	baseQuery,
	reducerPath: 'apiSlice',
	keepUnusedDataFor: 0,
	endpoints: () => ({}),
})
