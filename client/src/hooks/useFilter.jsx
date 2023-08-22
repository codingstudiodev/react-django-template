import { useState } from 'react'

const useFilter = initial => {
	const [filter, setFilter] = useState(initial)

	const onChange = e => {
		const { name, value } = e.target
		setFilter(currentData => ({
			...currentData,
			[name]: value,
		}))
	}

	return [filter, setFilter, onChange]
}

export default useFilter
