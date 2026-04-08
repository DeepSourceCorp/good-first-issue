export const useOpenRepoId = () => useState('openRepoId', () => null)
export const useStarsFilter = () => useState('starsFilter', () => 0)  // minimum stars
export const useActivityFilter = () => useState('activityFilter', () => null)  // days threshold
export const useIssueCountFilter = () => useState('issueCountFilter', () => null)  // '1-3', '4-10', '11-20', '20+'
