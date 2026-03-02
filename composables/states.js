/**
 * Composable function to manage the open repository ID state.
 *
 * @returns {object} The reactive openRepoId state.
 */
export const useOpenRepoId = () => useState('openRepoId', () => null);
